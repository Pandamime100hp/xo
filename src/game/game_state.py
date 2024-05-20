from src.enums import State


class GameState:
    state: State

    def __init__(self) -> None:
        """
        Object which handles the games current state. Game is 
        initialised in a WELCOME state, presenting the player with 
        a How-To tutorial.
        """
        self.state = State.WELCOME
