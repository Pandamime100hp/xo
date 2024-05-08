from src.actors import Person
from src.enums import XOSymbol


class Player(Person):
    def __init__(self, symbol: XOSymbol, nickname: str) -> None:
        """_summary_

        Args:
            symbol (XOSymbol): _description_
            nickname (str): _description_
        """
        super().__init__(symbol=symbol, nickname=nickname)
