import unittest

from src import Board
from src import XOSymbol


class TestBoard(unittest.TestCase):

    board: Board

    def setUp(self):
        """Sets up an initial environment for the board object."""
        self.board = Board()

    def tearDown(self):
        """Tidies up the board object so everything is clean for the next test."""
        self.board = None

    def test_fill_header(self):
        """Validates the generation of the header of the board."""
        self.board = Board()
        self.board.board = ""
        self.board._fill_header()
        self.assertEqual("      1   2   3\n", self.board.board)

    def test_fill_board_row_empty(self):
        """Validates the generation of a row with no tiles filled."""
        self.board = Board()
        self.board.board = ""
        self.board._fill_row_empty(row_id=0)
        self.assertEqual("  1 |   |   |   |\n", self.board.board)

    def test_fill_board_row(self):
        """Validates the generation of a row with tiles filled."""
        self.board = Board()
        self.board.board = ""
        tiles: list[list[XOSymbol]] = [[XOSymbol.X, XOSymbol.O, XOSymbol.X]]
        self.board._fill_row(row_id=0, tiles=tiles)
        self.assertEqual("  1 | X | O | X |\n", self.board.board)

    def test_board(self):
        """Validate that a board is built correctly from initialisation."""
        _board: str = "      1   2   3\n    *---*---*---*\n  1 |   |   |   |\n    *---*---*---*\n  2 |   |   |   |\n    *---*---*---*\n  3 |   |   |   |\n    *---*---*---*\n"
        self.assertEqual(_board, self.board.board)

    def test_full_filled_board(self):
        """Validates that a board is built correctly with all tiles filled."""
        _board: str = "      1   2   3\n    *---*---*---*\n  1 | X | O | X |\n    *---*---*---*\n  2 | O | X | O |\n    *---*---*---*\n  3 | X | O | X |\n    *---*---*---*\n"
        self.board = Board()
        tiles: list[list[XOSymbol]] = [[XOSymbol.X, XOSymbol.O, XOSymbol.X],
                                       [XOSymbol.O, XOSymbol.X, XOSymbol.O],
                                       [XOSymbol.X, XOSymbol.O, XOSymbol.X]]
        self.board.update_board(tiles=tiles)
        self.assertEqual(_board, self.board.board)


if __name__ == "__main__":
    unittest.main()