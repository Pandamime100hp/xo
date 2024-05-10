from src.board import Board
from src.controller import Controller
from src.game.game_state import GameState


class Game:
    """_summary_
    """
    
    def __init__(self) -> None:
        """_summary_
        """

        self.game_state: GameState = GameState()
        self.controller: Controller = Controller()
        self.board: Board = Board()

        self.states: dict = {
            0: self.welcome,
            1: self.new_round,
            2: self.play_round,
            3: self.end_round,
            4: self.exit
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
        self.game_state.set_state(4)
        print("Exit")
        return 0

    def run(self) -> None:
        """Executes the games main loop."""
        self.game_state.set_state(0)

        while not self.game_state.get_state(4):
            self.states[self.game_state.state.value]()
