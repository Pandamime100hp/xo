from abc import ABC

from . import XOSymbol


class Person(ABC):
    symbol: XOSymbol
    nickname: str
    score: int

    def __init__(self, symbol: XOSymbol, nickname: str) -> None:
        """Base class representing a Player or Enemy.

        Args:
            symbol (XOSymbol): Person symbol specified by XOSymbol enum.
            nickname (str): Person nickname.
        """
        self.symbol = symbol
        self.nickname = nickname
        self.score = 0

    def increment_score(self) -> None:
        """Increase the score of the person."""
        self.score += 1
