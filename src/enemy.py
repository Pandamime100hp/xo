from person import Person
from enums import XOSymbol


class Enemy(Person):
    def __init__(self, symbol: XOSymbol, nickname: str) -> None:
        super().__init__(symbol=symbol, nickname=nickname)
