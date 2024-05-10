import unittest

from src.game import Game

class TestGame(unittest.TestCase):
    game: Game

    def setUp(self) -> None:
        self.game = Game()
    
    def tearDown(self) -> None:
        self.game = None
    
    def test_welcome(self):
        pass

    def test_new_round(self):
        pass

    def test_play_round(self):
        pass

    def test_end_round(self):
        pass

    def test_exit_success(self):
        return_int: int = self.game.exit()
        self.assertEqual(0, return_int)