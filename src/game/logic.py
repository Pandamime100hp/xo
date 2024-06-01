from src.actors.enemy import Enemy
from src.actors.player import Player
from src.controller import Controller
from src.enums import State, XOSymbol
from src.game.game_state import GameState


class Logic:
    def __init__(self) -> None:
        """Object that handles the games workflow based on the current game state."""

        self.game_state: GameState = GameState()
        self.controller: Controller = Controller()

        self.game_state_actions: dict = {
            State.WELCOME: self.welcome,
            State.NEW_ROUND: self.new_round,
            State.PLAY_ROUND: self.play_round,
            State.END_ROUND: self.end_round,
            State.EXIT: self.exit
        }

    def welcome(self):
        """
        Function which handles the WELCOME state, introducing the player to the 
        game.
        """

        print("Welcome, choose your symbol!")
        user_input = self.controller.get_input()
        
        player_symbol: XOSymbol = XOSymbol.X if user_input == "X" else XOSymbol.O
        enemy_symbol: XOSymbol = XOSymbol.O if player_symbol == XOSymbol.X else XOSymbol.X

        print("Excellent!")
        print("Next, choose your nickname!")
        user_input = self.controller.get_input()
        player_nickname: str = user_input

        self.game_state.player = Player(symbol=player_symbol, nickname=player_nickname)

        print("An absolute pleasure to meet you,", self.game_state.player.nickname)
        print("We must discuss the elephant in the room. No knight can battle with no enemy.")
        print("Who is your enemy?")
        user_input = self.controller.get_input()
        enemy_nickname = user_input

        self.game_state.enemy = Enemy(symbol=enemy_symbol, nickname=enemy_nickname)

        print("I see. Sounds like a formidable foe. Let the battle between good and evil begin!")

        self.game_state.state = State.NEW_ROUND

    def new_round(self):
        """
        Function which handles the NEW_ROUND state, which clears the state of 
        the last game to a fresh game.
        """
        print("New round")

    def play_round(self):
        """
        Function which handles the PLAY_ROUND state, which executes the logic to 
        continue the game in progress.
        """
        print("Play round")

    def end_round(self):
        """
        Function which handles the END_ROUND state, which outputs the previous 
        rounds results and an options window.
        """
        print("End round")

    def exit(self) -> None:
        """
        Function which handles the EXIT state, which exits the games main loop 
        and returns the games exit reason using an integer code.
        """
        self.game_state.state = State.EXIT



        # if current_state == State.WELCOME:
        #     - choose your symbol 
        #         - state == new round
        #     - exit
        #         - state == exit
        # elif current_state == State.NEW_ROUND:
        #     - sets all objects to null
        #         - state == play round
        #     - exit
        #         - state == exit
        # elif current_state == State.PLAY_ROUND:
        #     - set tile with symbol
        #         - state == play round
        #     - surrender
        #         - state == end round
        #     - exit
        # elif current_state == State.END_ROUND:
        #     - play new round
        #         - state == new round
        #     - exit
        # else:
        #     - exit