from src.board import Board
from src.controller import Controller
from src.enums import State
from src.game.game_state import GameState


class Game:
    """Object that encapsulate all components of the game and runs the main loop."""

    exit_int: int = 0
    
    def __init__(self) -> None:
        """
        Builds the framework of the Game with a GameState, Controller and Board. 
        The Game also initialises the different states the game enters and 
        associates each state with a function for the respective state.
        """

        self.game_state: GameState = GameState()
        self.controller: Controller = Controller()
        self.board: Board = Board()

        self.states: dict = {
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
        print("Welcome")
        user_input = self.controller.get_input()

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

    def run(self) -> int:
        """Executes the games main loop."""
        while self.game_state.state != State.EXIT:
            self.states[self.game_state.state]()

        return self.exit_int
