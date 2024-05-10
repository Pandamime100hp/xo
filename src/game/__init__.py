from src.board import Board
from src.controller import Controller
from src.enums import State
from src.game.game_state import GameState


class Game:
    """_summary_
    """

    exit_int: int = 0
    
    def __init__(self) -> None:
        """_summary_
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
        """_summary_
        """
        print("Welcome")

    def new_round(self):
        """_summary_
        """
        print("New round")

    def play_round(self):
        """_summary_
        """
        print("Play round")

    def end_round(self):
        """_summary_
        """
        print("End round")

    def exit(self) -> int:
        """_summary_
        """
        self.game_state.state = State.EXIT
        print("Exit")
        return 0

    def run(self) -> int:
        """Executes the games main loop."""
        while self.game_state.state != State.EXIT:
            self.states[self.game_state.state.value]()

        return self.exit_int
