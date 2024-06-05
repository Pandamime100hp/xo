from src.actors.enemy import Enemy
from src.actors.player import Player
from src.enums import State, XOSymbol


class GameState:
    state: State
    player: Player
    enemy: Enemy
    current_actor: object
    tiles: list[list[XOSymbol]]
    score_player: int = 0
    score_enemy: int = 0

    def __init__(self) -> None:
        """
        Object which handles the games current state. Game is 
        initialised in a WELCOME state, presenting the player with 
        a How-To tutorial.
        """
        self.state = State.WELCOME

    def reset_round(self) -> None:
        """
        Resets the round by initializing the `tiles` attribute to a 3x3 grid of `XOSymbol.EMPTY`.
        
        Returns:
            None
        """
        self.tiles = [[XOSymbol.EMPTY for i in range(3)] for j in range(3)]

    def set_tile(self, x: int, y: int, symbol: XOSymbol) -> None:
        if self.tiles[x][y] == XOSymbol.EMPTY:
            self.tiles[x][y] = symbol
        else:
            raise ValueError(f"Tile X={x}, Y={y} is already occupied")
