from src.enums import XOSymbol


class Board:
    HEADER: str = "      1   2   3"
    ROW_SEP: str = "    *---*---*---*"
    COL_SEP: str = "  %d | %s | %s | %s |"
    EMPTY: str = " "

    board: str = ""

    def __init__(self) -> None:
        self.update_board()
        
    def update_board(self, tiles: list[list[XOSymbol]] = None) -> None:
        self.board = ""
        self._fill_header()

        for row_id in range(3):
            self._fill_row_separator()
            self._fill_tiles(row_id=row_id, tiles=tiles)
        self._fill_row_separator()

    def _fill_row_none(self, row_id: int) -> None:
        self.board += self.COL_SEP % (row_id + 1, self.EMPTY, self.EMPTY, self.EMPTY)
        self._fill_new_line()

    def _fill_row(self, row_id: int, tiles: list[list[XOSymbol]]) -> None:
        self.board += self.COL_SEP % (row_id + 1, tiles[row_id][0].value, tiles[row_id][1].value, tiles[row_id][2].value)
        self._fill_new_line()

    def _fill_header(self) -> None:
        self.board += self.HEADER
        self._fill_new_line()

    def _fill_tiles(self, row_id: int, tiles: list[list[XOSymbol]]) -> None:
        self._fill_row(row_id=row_id, tiles=tiles) if tiles else self._fill_row_none(row_id=row_id)

    def _fill_row_separator(self) -> None:
        self.board += self.ROW_SEP
        self._fill_new_line()

    def _fill_new_line(self) -> None:
        self.board += "\n"