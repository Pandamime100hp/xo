from src.actors import Person
from src.enums import XOSymbol


class Player(Person):
    def __init__(self, symbol: XOSymbol, nickname: str) -> None:
        """The Player class which is the main player in the game.

        Args:
            symbol (XOSymbol): _description_
            nickname (str): _description_
        """
        super().__init__(symbol=symbol, nickname=nickname)
