from src.enums import State


class GameState:
    state: State

    def __init__(self) -> None:
        """_summary_
        """
        self.state = State.WELCOME