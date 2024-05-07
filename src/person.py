from abc import ABC

from . import XOSymbol


class Person(ABC):
    symbol: XOSymbol
    nickname: str
    score: int

    def __init__(self, symbol: XOSymbol, nickname: str) -> None:
        self.symbol = symbol
        self.nickname = nickname
        self.score = 0

    def increment_score(self) -> None:
        self.score += 1
