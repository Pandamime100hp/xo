from src.board import Board
from src.controller import Controller
from src.enums import State
from src.game.logic import Logic


class Game:
    """Game class that handles the games workflow based on the current game state."""

    exit_int: int = 0
    
    def __init__(self) -> None:
        """
        Builds the framework of the Game with a GameState, Controller and Board. 
        The Game also initialises the different states the game enters and 
        associates each state with a function for the respective state.

        Returns:
            None
        """

        self.logic: Logic = Logic()
        self.controller: Controller = Controller()
        self.board: Board = Board()

    def run(self) -> int:
        """Executes the games main loop.
        
        Returns:
            int: Exit code
        """
        while self.logic.game_state.state != State.EXIT:
            self.logic.game_state_actions[self.logic.game_state.state]()

        return self.exit_int
