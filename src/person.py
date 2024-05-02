from abc import ABC, abstractmethod

from . import XOSymbol


class Person(ABC):
    symbol: XOSymbol
    nickname: str
    score: int

    def __init__(self, symbol: XOSymbol, nickname: str) -> None:
        self.symbol = symbol
        self.nickname = nickname
        self.score = 0
    
    @property
    @abstractmethod
    def symbol(self) -> XOSymbol:
        pass

    @property
    @abstractmethod
    def nickname(self) -> str:
        pass

    @property
    @abstractmethod
    def score(self) -> int:
        pass

    def increment_score(self) -> None:
        self.score += 1
