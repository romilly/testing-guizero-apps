#!/usr/bin/env python3
import unittest
from guizero import PushButton
from tictactoe import TicTacToeApp


def push(button: PushButton) -> None:
    button.tk.invoke()


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.app = TicTacToeApp()

    def setUp(self) -> None:
        self.app.reset_board()
        self.app.winner = None
        self.app.turn = 'X'
        self.app.message.value = 'It is your turn, X'

    def message_value(self):
        return self.app.message.value

    def play(self, x, y):
        push(self.app.square(x, y))

    def test_shows_player_X_at_start(self):
        self.assertEqual(self.message_value(), 'It is your turn, X')

    def test_turn_changes_after_player_moves(self):
        self.assertEqual(self.message_value(), 'It is your turn, X')
        self.play(0, 0)
        self.assertEqual(self.message_value(), 'It is your turn, O')

    def test_knows_if_x_has_won(self):
        self.assertEqual(self.message_value(), 'It is your turn, X')
        self.play(0, 0)
        self.play(0, 1)
        self.play(1, 0)
        self.play(0, 2)
        self.play(2, 0)
        self.assertEqual(self.message_value(), 'X wins!')

    def test_knows_if_o_has_won(self):
        self.assertEqual(self.message_value(), 'It is your turn, X')
        self.play(0, 0)
        self.play(0, 1)
        self.play(1, 0)
        self.play(1, 1)
        self.play(1, 2)
        self.play(2, 1)
        self.assertEqual(self.message_value(), 'O wins!')

    def test_recognises_draw(self):
        self.play(0, 0)
        self.play(1, 1)
        self.play(2, 2)
        self.play(0, 1)
        self.play(2, 1)
        self.play(2, 0)
        self.play(0, 2)
        self.play(1, 2)
        self.play(1, 0)
        self.assertEqual("It's a draw", self.message_value())

    def show_board(self):
        for x in range(3):
            print([self.app.board_squares[x][y].text for y in range(3)])
        print(' ')


if __name__ == '__main__':
    unittest.main()
