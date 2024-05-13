import unittest

from src.game import Game

class TestGame(unittest.TestCase):
    game: Game

    def setUp(self) -> None:
        self.game = Game()
    
    def tearDown(self) -> None:
        self.game = None
    
    @unittest.skip
    def test_welcome(self):
        pass

    @unittest.skip
    def test_new_round(self):
        pass

    @unittest.skip
    def test_play_round(self):
        pass

    @unittest.skip
    def test_end_round(self):
        pass

    def test_exit_success(self):
        self.game.exit()
        self.assertEqual(0, self.game.exit_int)