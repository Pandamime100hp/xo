from src.enums import XOSymbol


class Board:
    
    HEADER: str = "      1   2   3"
    ROW_SEP: str = "    *---*---*---*"
    COL_SEP: str = "  %d | %s | %s | %s |"
    EMPTY: str = " "

    board: str = ""

    def __init__(self) -> None:
        """Board class that generates the board drawn on screen. The board tiles are populated with symbols by each person."""
        self.update_board()
        
    def update_board(self, tiles: list[list[XOSymbol]] = None) -> None:
        """Refresh the board with latest tiles.

        Args:
            tiles (list[list[XOSymbol]], optional): 2D array of tiles with person symbols filled. Defaults to None.
        """
        self.board = ""
        self._fill_header()

        for row_id in range(3):
            self._fill_row_separator()
            self._fill_tiles(row_id=row_id, tiles=tiles)
        self._fill_row_separator()

    def _fill_row_empty(self, row_id: int) -> None:
        """Prints row with empty tiles.

        Args:
            row_id (int): Current row being processed.
        """
        self.board += self.COL_SEP % (row_id + 1, self.EMPTY, self.EMPTY, self.EMPTY)
        self._fill_new_line()

    def _fill_row(self, row_id: int, tiles: list[list[XOSymbol]]) -> None:
        """Prints row of populated tiles.

        Args:
            row_id (int): Current row being processed.
            tiles (list[list[XOSymbol]]): 2D array of tiles with person symbols filled.
        """
        self.board += self.COL_SEP % (row_id + 1, tiles[row_id][0].value, tiles[row_id][1].value, tiles[row_id][2].value)
        self._fill_new_line()

    def _fill_header(self) -> None:
        """Prints header row."""
        self.board += self.HEADER
        self._fill_new_line()

    def _fill_tiles(self, row_id: int, tiles: list[list[XOSymbol]]) -> None:
        """Prints row of tiles.

        Args:
            row_id (int): Current row being processed.
            tiles (list[list[XOSymbol]]): 2D array of tiles with person symbols filled.
        """
        self._fill_row(row_id=row_id, tiles=tiles) if tiles else self._fill_row_empty(row_id=row_id)

    def _fill_row_separator(self) -> None:
        """Prints a new row separator."""
        self.board += self.ROW_SEP
        self._fill_new_line()

    def _fill_new_line(self) -> None:
        """Prints a new line."""
        self.board += "\n"