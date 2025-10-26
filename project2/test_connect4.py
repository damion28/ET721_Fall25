import unittest
from io import StringIO
from unittest.mock import patch
from main import Connect4

class TestConnect4PrintBoard(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_board_initial(self, mock_stdout):
        game = Connect4()
        game.print_board()
        output = mock_stdout.getvalue()

        self.assertIn("1 2 3 4 5 6 7", output)

        self.assertEqual(output.count('| | | | | | | |'), 6)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_board_after_move(self, mock_stdout):
        game = Connect4()
        game.drop_chip(1)
        game.print_board()
        output = mock_stdout.getvalue()

        self.assertIn('X', output)

        self.assertIn("Current Board:", output)
        self.assertIn("1 2 3 4 5 6 7", output)

if __name__ == '__main__':
    unittest.main()
