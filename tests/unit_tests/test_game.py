import unittest
from unittest.mock import MagicMock, patch

from src.enums import State
from src.game import Game
from src.game.game_state import GameState

class TestGame(unittest.TestCase):

    def setUp(self) -> None:
        """Set up the necessary mocks and the Game instance for testing."""
        self.mock_game_state = MagicMock(spec=GameState)
        self.mock_controller = MagicMock()
        self.mock_board = MagicMock()

        with patch('src.game.GameState', return_value=self.mock_game_state), \
             patch('src.game.Controller', return_value=self.mock_controller), \
             patch('src.game.Board', return_value=self.mock_board):
            self.game = Game()
    
    def tearDown(self) -> None:
        self.game = None

    def test_initialization(self):
        """Test that the game initializes with the correct states and components."""
        self.assertIsInstance(self.game.game_state, GameState)
        self.assertIsInstance(self.game.controller, MagicMock)
        self.assertIsInstance(self.game.board, MagicMock)
        self.assertEqual(self.game.exit_int, 0)
        self.assertIn(State.WELCOME, self.game.states)
        self.assertIn(State.NEW_ROUND, self.game.states)
        self.assertIn(State.PLAY_ROUND, self.game.states)
        self.assertIn(State.END_ROUND, self.game.states)
        self.assertIn(State.EXIT, self.game.states)
    
    def test_welcome(self):
        """Test the welcome state function."""
        with patch('builtins.print') as mock_print:
            self.game.welcome()
            mock_print.assert_called_once_with("Welcome")

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

    @unittest.skip
    def test_run(self, mock_welcome, mock_new_round, mock_play_round, mock_end_round, mock_exit):
            self.mock_game_state.state = State.WELCOME

            self.mock_game_state.state.return_value = State.WELCOME

            self.game.run()

            mock_welcome.assert_called_once()
        # """Test the main game loop."""
        # with patch.object(self.game, 'welcome') as mock_welcome, \
        #      patch.object(self.game, 'new_round') as mock_new_round, \
        #      patch.object(self.game, 'play_round') as mock_play_round, \
        #      patch.object(self.game, 'end_round') as mock_end_round, \
        #      patch.object(self.game, 'exit') as mock_exit:

            # # Define a sequence of states to simulate the game progression
            # state_sequence = [State.WELCOME, State.NEW_ROUND, State.PLAY_ROUND, State.END_ROUND, State.EXIT]
            # state_iterator = iter(state_sequence)

            # # Function to get the next state from the sequence
            # def next_state():
            #     try:
            #         self.mock_game_state.state = next(state_iterator)
            #     except StopIteration:
            #         self.mock_game_state.state = State.EXIT

            # # Override the run method for testing
            # def run_with_state_transition():
            #     # Patch the game state's state attribute to transition states
                
            #     self.mock_game_state.state.side_effect = next_state

            #     while self.mock_game_state.state != State.EXIT:
            #         self.game.states[self.mock_game_state.state]
            #         next_state()

            # with patch.object(self.game, 'run', new=run_with_state_transition):
            #     self.game.run()

            # mock_welcome.assert_called_once()
            # mock_new_round.assert_called_once()
            # mock_play_round.assert_called_once()
            # mock_end_round.assert_called_once()
            # mock_exit.assert_called_once()

if __name__ == '__main__':
    unittest.main()