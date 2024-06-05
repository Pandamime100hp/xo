import random
import time
from src.actors.enemy import Enemy
from src.actors.player import Player
from src.board import Board
from src.controller import Controller
from src.enums import State, XOSymbol
from src.game.game_state import GameState
from src.helpers import clear_screen


class Logic:
    def __init__(self) -> None:
        """Object that handles the games workflow based on the current game state."""

        self.game_state: GameState = GameState()
        self.controller: Controller = Controller()
        self.board: Board = Board()

        self.game_state_actions: dict = {
            State.WELCOME: self.welcome,
            State.NEW_ROUND: self.new_round,
            State.PLAY_ROUND: self.play_round,
            State.END_ROUND: self.end_round,
            State.EXIT: self.exit
        }

    def player_symbol_choice(self) -> str:
        """
        Prompts the user to choose their symbol (X or O) and validates the input.

        Returns:
            str: The chosen symbol (X or O).
        """
        print("Please choose your symbol! (X/O)")
        user_input = self.controller.get_input()

        if user_input not in ["X", "O"]:
            clear_screen()
            print("Invalid input. Please enter X or O.")
            user_input = self.player_symbol_choice()
        return user_input

    def introduction(self) -> tuple[XOSymbol, XOSymbol]:
        """
        Introduces the player to the game and prompts them to choose their symbol.
        
        Returns:
            tuple[XOSymbol, XOSymbol]: A tuple containing the player's symbol and the enemy's symbol.
        """
        clear_screen()
        print("Welcome knight!")

        symbol: str = self.player_symbol_choice()
        
        player_symbol: XOSymbol = self._set_player_symbol(user_input=symbol)
        enemy_symbol: XOSymbol = self._set_enemy_symbol(user_input=symbol)

        return player_symbol, enemy_symbol
    
    def set_player_nickname(self, player_symbol: XOSymbol) -> str:
        """
        Set the player's nickname by prompting the user for input.

        This function clears the screen, displays a message to the user, and then prompts the user to enter their nickname. The entered nickname is then returned as a string.

        Returns:
            str: The player's nickname.
        """
        print(f"Ah, so you have chosen the path of the {player_symbol.value}. Excellent choice!")
        print("Next, choose your nickname!")
        player_nickname = self.controller.get_input()
        if len(player_nickname) == 0:
            clear_screen()
            print("Your nickname cannot be empty. Please enter a nickname.")
            return self.set_player_nickname()
        if len(player_nickname) > 15:
            clear_screen()
            print("Your nickname is too long. Please enter a nickname that is less than 15 characters long.")
            return self.set_player_nickname()
        return player_nickname
    
    def set_enemy_nickname(self, enemy_symbol: XOSymbol) -> str:
        """
        Sets the nickname of the enemy by prompting the user for input.

        This function clears the screen, displays a message to the user, and then prompts the user to enter their enemy's nickname. The entered nickname is then returned as a string.

        Returns:
            str: The enemy's nickname.
        """
        print("We must discuss the elephant in the room. No knight can do battle with no enemy.")
        print(f"Your enemie are the {enemy_symbol.value}. What is your enemy's nickname?")
        enemy_nickname = self.controller.get_input()
        if len(enemy_nickname) == 0:
            clear_screen()
            print("Your enemy's nickname cannot be empty. Please enter a nickname.")
            return self.set_enemy_nickname()
        if len(enemy_nickname) > 15:
            clear_screen()
            print("Your enemy's nickname is too long. Please enter a nickname that is less than 15 characters long.")
            return self.set_enemy_nickname()
        return enemy_nickname
    
    def let_the_game_begin(self) -> None:
        """
        Let the game begin by printing a message and transitioning to the NEW_ROUND state.

        This function clears the screen, displays a message to the user, sets the next actor's turn randomly, prints the current actor's nickname, and transitions to the NEW_ROUND state after a delay of 4 seconds.

        Returns:
            None
        """
        clear_screen()
        print("I see. Sounds like a formidable foe. Let the battle between good and evil begin!")
        self.set_next_actor_turn_randomly()
        print(f"It is {self.game_state.current_actor.nickname}'s turn!")
        time.sleep(4)
        self.game_state.state = State.NEW_ROUND

    def _check_winner_horizontal(self) -> bool:
        """
        Check if there is a horizontal winner in the game state.

        x  x  x

        This function checks if there is a horizontal winner in the game state by comparing the values of the tiles in
        the game board. A horizontal winner occurs when the same symbol is present in the same row of the game board.

        Returns:
            bool: True if there is a horizontal winner, False otherwise.
        """
        return self.game_state.tiles[0][0] == self.game_state.tiles[0][1] == self.game_state.tiles[0][2] != XOSymbol.EMPTY or \
           self.game_state.tiles[1][0] == self.game_state.tiles[1][1] == self.game_state.tiles[1][2] != XOSymbol.EMPTY or \
           self.game_state.tiles[2][0] == self.game_state.tiles[2][1] == self.game_state.tiles[2][2] != XOSymbol.EMPTY

    def _check_winner_vertical(self) -> bool:
        """
        Check if there is a vertical winner in the game state.

        x
        x
        x

        This function checks if there is a vertical winner in the game state by comparing the values of the tiles in
        the game board. A vertical winner occurs when the same symbol is present in the same column of the game board.

        Returns:
            bool: True if there is a vertical winner, False otherwise.
        """
        return self.game_state.tiles[0][0] == self.game_state.tiles[1][0] == self.game_state.tiles[2][0] != XOSymbol.EMPTY or \
           self.game_state.tiles[0][1] == self.game_state.tiles[1][1] == self.game_state.tiles[2][1] != XOSymbol.EMPTY or \
           self.game_state.tiles[0][2] == self.game_state.tiles[1][2] == self.game_state.tiles[2][2] != XOSymbol.EMPTY

    def _check_winner_cross(self) -> bool:
        """
        Check if there is a diagonal winner in the game state.

        x                  x
          x      or      x
            x          x

        This function checks if there is a diagonal winner in the game state by comparing the values of the tiles in
        the game board. A diagonal winner occurs when the same symbol is present in the same diagonal of the game board.

        Returns:
            bool: True if there is a diagonal winner, False otherwise.
        """
        return self.game_state.tiles[0][0] == self.game_state.tiles[1][1] == self.game_state.tiles[2][2] != XOSymbol.EMPTY or \
           self.game_state.tiles[0][2] == self.game_state.tiles[1][1] == self.game_state.tiles[2][0] != XOSymbol.EMPTY

    def check_for_winner(self) -> None:
        """
        Check if there is a winner in the game state.

        This function checks if there is a winner in the game state by calling the private methods `_check_winner_vertical()`, `_check_winner_horizontal()`, and `_check_winner_cross()`. If any of these methods return `True`, it sets the state of the game to `State.END_ROUND`.

        Returns:
            None: This function does not return anything.
        """
        
        if self._check_winner_vertical() or self._check_winner_horizontal() or self._check_winner_cross():
            return True
        return False

    def _set_player_symbol(self, user_input: str) -> XOSymbol:
        """
        Set the symbol for the player based on the user input.
        
        Parameters:
            user_input (str): The user input string.
        
        Returns:
            XOSymbol: The symbol for the player. Returns XOSymbol.X if the user input is "X", otherwise returns XOSymbol.O.
        """
        return XOSymbol.X if user_input == "X" else XOSymbol.O
    
    def _set_enemy_symbol(self, user_input: str) -> XOSymbol:
        """
        Set the symbol for the enemy based on the user input.
        
        Parameters:
            user_input (str): The user input string.
        
        Returns:
            XOSymbol: The symbol for the enemy. Returns XOSymbol.O if the user input is "X", otherwise returns XOSymbol.X.
        """
        return XOSymbol.O if user_input == "X" else XOSymbol.X
    
    def set_next_actor_turn_randomly(self) -> None:
        """
        Sets the next actor to take their turn in the game.

        This function selects a random actor from the list of players and the enemy and assigns it to the `current_actor` attribute of the `game_state` object.

        Returns:
            None: This function does not return anything.
        """
        self.game_state.current_actor = random.choice([self.game_state.player, self.game_state.enemy])

    def set_next_actor_turn(self) -> None:
        """
        Sets the next actor to take their turn in the game.

        This function selects the next actor based on the current actor. If the current actor is the enemy, the next actor will be the player. Otherwise, the next actor will be the enemy. The selected actor is then assigned to the `current_actor` attribute of the `game_state` object.

        Returns:
            None: This function does not return anything.
        """
        self.game_state.current_actor = self.game_state.player if self.game_state.current_actor == self.game_state.enemy else self.game_state.enemy

    def get_input_coord(self, axis: str) -> int:
        print(f"Your turn, {self.game_state.player.nickname}!")
        print(f"Please enter a tile position on the {axis} axis (1-3):")
        coord_str: str = self.controller.get_input()
        if int(coord_str) < 1 or int(coord_str) > 3:
            clear_screen()
            self.board.draw()
            print("Invalid input. Please enter a number between 1 and 3.")
            return self.get_input_coord(axis)
        return int(coord_str) - 1

    def play_player_turn(self) -> None:

        x = self.get_input_coord("X")
        
        clear_screen()
        self.board.draw()

        y = self.get_input_coord("Y")
        
        try:
            self.game_state.set_tile(x, y, self.game_state.player.symbol)
        except ValueError:
            print(f"Tile X={x}, Y={y} is already occupied. Please choose another tile.")
            self.play_player_turn()

    def play_enemy_turn(self) -> None:
        x = random.randint(0, 2)
        y = random.randint(0, 2)

        try:
            self.game_state.set_tile(x, y, self.game_state.enemy.symbol)
        except ValueError:
            self.play_enemy_turn()

    def welcome(self):
        """
        Function which handles the WELCOME state, introducing the player to the game.

        This function prompts the user to choose their symbol and nickname, creates Player and Enemy objects with the chosen symbols and nicknames, and transitions to the NEW_ROUND state.

        Returns:
            None
        """

        player_symbol, enemy_symbol = self.introduction()
        clear_screen()
        player_nickname = self.set_player_nickname(player_symbol=player_symbol)
        clear_screen()
        enemy_nickname = self.set_enemy_nickname(enemy_symbol=enemy_symbol)

        self.game_state.player = Player(symbol=player_symbol, nickname=player_nickname)
        self.game_state.enemy = Enemy(symbol=enemy_symbol, nickname=enemy_nickname)

        self.let_the_game_begin()

    def new_round(self) -> None:
        """
        Resets the game state to a fresh round and sets the state to PLAY_ROUND.

        This function clears the game state by calling the `reset_round` method of the `game_state` object. It then sets the state of the game to `State.PLAY_ROUND`.

        Returns:
            None
        """
        self.game_state.reset_round()
        self.game_state.state = State.PLAY_ROUND


    def play_round(self) -> None:
        """
        Function which handles the PLAY_ROUND state, which executes the logic to continue the game in progress.

        This function continuously updates the game state and the board until the current state is not END_ROUND.
        It prompts the player for input to enter a tile position on the X and Y axes, and sets the tile with the player's symbol.
        If the tile is already occupied, it prompts the player to choose another tile.
        After setting the tile, it checks for a winner.

        Returns:
            None
        """
        while self.game_state.state != State.END_ROUND:
            self.board.update_board(self.game_state.tiles)

            clear_screen()
            self.board.draw()
            if self.game_state.current_actor == self.game_state.player:
                self.play_player_turn()
            else:
                self.play_enemy_turn()
            if self.check_for_winner():
                self.game_state.state = State.END_ROUND
            self.set_next_actor_turn()

    def end_round(self):
        """
        Function which handles the END_ROUND state, which outputs the previous 
        rounds results and an options window.

        # if current_state == State.END_ROUND:
        #     - play new round
        #         - state == new round
        #     - exit
        """
        clear_screen()
        self.game_state.current_actor.increment_score()
        print(f"{self.game_state.current_actor.nickname} has won the round!")
        print(f"Your score: {self.game_state.player.score}", f"Enemy score: {self.game_state.enemy.score}")
        print("Do you want to play again? (Y/N)")
        decision: str = self.controller.get_input()
        if decision == "Y":
            self.game_state.state = State.NEW_ROUND
        else:
            self.game_state.state = State.EXIT

    def exit(self) -> None:
        """
        Function which handles the EXIT state, which exits the games main loop 
        and returns the games exit reason using an integer code.
        
        # else:
        #     - exit
        """
        self.game_state.state = State.EXIT



        
        
        
        
       