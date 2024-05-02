from abc import ABC

from . import XOSymbol


class Person(ABC):
    symbol: XOSymbol
    nickname: str
    score: int
    