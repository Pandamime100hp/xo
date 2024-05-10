from enum import Enum

class XOSymbol(Enum):
    X = "X"
    O = "O"


class State(Enum):
    WELCOME = 0
    NEW_ROUND = 1
    PLAY_ROUND = 2
    END_ROUND = 3
    EXIT = 4
