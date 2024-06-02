import random
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

    def introduction(self) -> tuple[XOSymbol, XOSymbol]:
        """
        Introduces the player to the game and prompts them to choose their symbol.
        
        Returns:
            tuple[XOSymbol, XOSymbol]: A tuple containing the player's symbol and the enemy's symbol.
        """
        clear_screen()
        print("Welcome, choose your symbol!")
        user_input = self.controller.get_input()
        
        player_symbol: XOSymbol = self._set_player_symbol(user_input=user_input)
        enemy_symbol: XOSymbol = self._set_enemy_symbol(user_input=user_input)

        return player_symbol, enemy_symbol
    
    def set_player_nickname(self) -> str:
        """
        Set the player's nickname by prompting the user for input.

        This function clears the screen, displays a message to the user, and then prompts the user to enter their nickname. The entered nickname is then returned as a string.

        Returns:
            str: The player's nickname.
        """
        clear_screen()
        print("Excellent!")
        print("Next, choose your nickname!")
        player_nickname = self.controller.get_input()
        return player_nickname
    
    def set_enemy_nickname(self) -> str:
        """
        Sets the nickname of the enemy by prompting the user for input.

        This function clears the screen, displays a message to the user, and then prompts the user to enter their enemy's nickname. The entered nickname is then returned as a string.

        Returns:
            str: The enemy's nickname.
        """
        clear_screen()
        print("We must discuss the elephant in the room. No knight can battle with no enemy.")
        print("Who is your enemy?")
        enemy_nickname = self.controller.get_input()
        return enemy_nickname
    
    def let_the_game_begin(self) -> None:
        """
        Let the game begin by printing a message and transitioning to the NEW_ROUND state.

        Returns:
            None
        """
        print("I see. Sounds like a formidable foe. Let the battle between good and evil begin!")
        clear_screen()
        self.set_next_actor_turn_randomly()
        self.game_state.state = State.NEW_ROUND

    def _check_if_tile_empty(self, x: int, y: int) -> bool:
        """
        Check if the tile at the given coordinates is empty.

        Parameters:
            x (int): The x-coordinate of the tile.
            y (int): The y-coordinate of the tile.

        Returns:
            bool: True if the tile is empty, False otherwise.
        """
        return self.game_state.tiles[x][y] == XOSymbol.EMPTY
    
    def _check_if_next_tile_equal_horizontal(self, x: int, y: int) -> bool:
        """
        Check if the tile at the given coordinates is equal to the tile horizontally adjacent to it.

        Parameters:
            x (int): The x-coordinate of the tile.
            y (int): The y-coordinate of the tile.

        Returns:
            bool: True if the tile is equal to the tile horizontally adjacent to it, False otherwise.
        """
        return self.game_state.tiles[x][y] == self.game_state.tiles[x+1][y]
    
    def _check_if_next_tile_equal_vertical(self, x: int, y: int) -> bool:
        """
        Check if the tile at the given coordinates is equal to the tile vertically adjacent to it.

        Parameters:
            x (int): The x-coordinate of the tile.
            y (int): The y-coordinate of the tile.

        Returns:
            bool: True if the tile is equal to the tile vertically adjacent to it, False otherwise.
        """
        return self.game_state.tiles[x][y] == self.game_state.tiles[x][y+1]
    
    def _check_if_next_tile_equal_cross(self, x: int, y: int) -> bool:
        """
        Check if the tile at the given coordinates is equal to the tile diagonally adjacent to it.

        Parameters:
            x (int): The x-coordinate of the tile.
            y (int): The y-coordinate of the tile.

        Returns:
            bool: True if the tile is equal to the tile diagonally adjacent to it, False otherwise.
        """
        return self.game_state.tiles[x][y] == self.game_state.tiles[x+1][y+1]

    def _check_winner_horizontal(self) -> bool:
        """
        Check if there is a horizontal winner in the game state.

        This function checks if there is a horizontal winner in the game state by comparing the values of the tiles in
        the game board. A horizontal winner occurs when the same symbol is present in the same row of the game board.

        Returns:
            bool: True if there is a horizontal winner, False otherwise.
        """
        if self.game_state.tiles[0][0] == self.game_state.tiles[0][1] == self.game_state.tiles[0][2] or \
           self.game_state.tiles[1][0] == self.game_state.tiles[1][1] == self.game_state.tiles[1][2] or \
           self.game_state.tiles[2][0] == self.game_state.tiles[2][1] == self.game_state.tiles[2][2]:
            return True
        return False

    def _check_winner_vertical(self) -> bool:
        """
        Check if there is a vertical winner in the game state.

        This function checks if there is a vertical winner in the game state by comparing the values of the tiles in
        the game board. A vertical winner occurs when the same symbol is present in the same column of the game board.

        Returns:
            bool: True if there is a vertical winner, False otherwise.
        """
        if self.game_state.tiles[0][0] == self.game_state.tiles[1][0] == self.game_state.tiles[2][0] or \
           self.game_state.tiles[0][1] == self.game_state.tiles[1][1] == self.game_state.tiles[2][1] or \
           self.game_state.tiles[0][2] == self.game_state.tiles[1][2] == self.game_state.tiles[2][2]:
            return True
        return False

    def _check_winner_cross(self) -> bool:
        """
        Check if there is a diagonal winner in the game state.

        This function checks if there is a diagonal winner in the game state by comparing the values of the tiles in
        the game board. A diagonal winner occurs when the same symbol is present in the same diagonal of the game board.

        Returns:
            bool: True if there is a diagonal winner, False otherwise.
        """
        if self.game_state.tiles[0][0] == self.game_state.tiles[1][1] == self.game_state.tiles[2][2] or \
           self.game_state.tiles[0][2] == self.game_state.tiles[1][1] == self.game_state.tiles[2][0]:
            return True
        return False

    def check_for_winner(self) -> None:
        """
        Check if there is a winner in the game state.

        This function checks if there is a winner in the game state by calling the private methods `_check_winner_vertical()`, `_check_winner_horizontal()`, and `_check_winner_cross()`. If any of these methods return `True`, it sets the state of the game to `State.END_ROUND`.

        Returns:
            None: This function does not return anything.
        """
        if self._check_winner_vertical() or self._check_winner_horizontal() or self._check_winner_cross():
            self.game_state.state = State.END_ROUND

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
        self.game_state.current_actor = self.game_state.player if self.game_state.current_actor ==self.game_state.enemy else self.game_state.enemy

    def get_input_coord(self, axis: str) -> int:
        print("Your turn,", self.game_state.player.nickname, "!")
        print(f"Please enter a tile position on the {axis} axis (1-3):")
        x = int(self.controller.get_input()) - 1

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


    def welcome(self):
        """
        Function which handles the WELCOME state, introducing the player to the game.

        This function prompts the user to choose their symbol and nickname, creates Player and Enemy objects with the chosen symbols and nicknames, and transitions to the NEW_ROUND state.

        Returns:
            None
        """

        player_symbol, enemy_symbol = self.introduction()
        player_nickname = self.set_player_nickname()
        enemy_nickname = self.set_enemy_nickname()

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
            self.check_for_winner()

    def end_round(self):
        """
        Function which handles the END_ROUND state, which outputs the previous 
        rounds results and an options window.

        # if current_state == State.END_ROUND:
        #     - play new round
        #         - state == new round
        #     - exit
        """
        
        print(f"{self.game_state.player.nickname} has won the round!")

    def exit(self) -> None:
        """
        Function which handles the EXIT state, which exits the games main loop 
        and returns the games exit reason using an integer code.
        
        # else:
        #     - exit
        """
        self.game_state.state = State.EXIT



        
        
        
        
       