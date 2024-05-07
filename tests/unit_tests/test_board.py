import unittest

from src import Board
from src import XOSymbol


class TestBoard(unittest.TestCase):

    board: Board

    def setUp(self):
        self.board = Board()

    def tearDown(self):
        self.board = None

    def test_board(self):
        _board: str = "      1   2   3\n    *---*---*---*\n  1 |   |   |   |\n    *---*---*---*\n  2 |   |   |   |\n    *---*---*---*\n  3 |   |   |   |\n    *---*---*---*\n"
        self.assertEqual(_board, self.board.board)

    def test_fill_header(self):
        self.board = Board()
        self.board.board = ""
        self.board._fill_header()
        self.assertEqual("      1   2   3\n", self.board.board)

    def test_fill_board_row_none(self):
        self.board = Board()
        self.board.board = ""
        self.board._fill_row_none(row_id=0)
        self.assertEqual("  1 |   |   |   |\n", self.board.board)

    def test_fill_board_row(self):
        self.board = Board()
        self.board.board = ""
        tiles: list[list[XOSymbol]] = [[XOSymbol.X, XOSymbol.O, XOSymbol.X]]
        self.board._fill_row(row_id=0, tiles=tiles)
        self.assertEqual("  1 | X | O | X |\n", self.board.board)

    def test_full_filled_board(self):
        _board: str = "      1   2   3\n    *---*---*---*\n  1 | X | O | X |\n    *---*---*---*\n  2 | O | X | O |\n    *---*---*---*\n  3 | X | O | X |\n    *---*---*---*\n"
        self.board = Board()
        tiles: list[list[XOSymbol]] = [[XOSymbol.X, XOSymbol.O, XOSymbol.X],
                                       [XOSymbol.O, XOSymbol.X, XOSymbol.O],
                                       [XOSymbol.X, XOSymbol.O, XOSymbol.X]]
        self.board.update_board(tiles=tiles)
        self.assertEqual(_board, self.board.board)


if __name__ == "__main__":
    unittest.main()