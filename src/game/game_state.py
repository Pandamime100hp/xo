from src.actors.enemy import Enemy
from src.actors.player import Player
from src.enums import State, XOSymbol


class GameState:
    state: State
    player: Player
    enemy: Enemy
    score_player: int = 0
    score_enemy: int = 0

    def __init__(self) -> None:
        """
        Object which handles the games current state. Game is 
        initialised in a WELCOME state, presenting the player with 
        a How-To tutorial.
        """
        self.state = State.WELCOME
