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

    def play(self, x, y, player):
        self.assertEqual(self.message_value(), 'It is your turn, %s' % player)
        push(self.app.square(x, y))

    def test_shows_player_X_at_start(self):
        self.assertEqual(self.message_value(), 'It is your turn, X')

    def test_turn_changes_after_player_moves(self):
        self.play(0, 0, 'X')
        self.assertEqual(self.message_value(), 'It is your turn, O')
        expected_board = """
        X-- 
        ---
        ---"""
        self.check_board(expected_board)

    def test_knows_if_x_has_won(self):
        self.play(0, 0, 'X')
        self.play(0, 1, 'O')
        self.play(1, 0, 'X')
        self.play(0, 2, 'O')
        self.play(2, 0, 'X')
        self.assertEqual(self.message_value(), 'X wins!')

    def test_knows_if_o_has_won(self):
        self.play(0, 0, 'X')
        self.play(0, 1, 'O')
        self.play(1, 0, 'X')
        self.play(1, 1, 'O')
        self.play(1, 2, 'X')
        self.play(2, 1, 'O')
        self.assertEqual(self.message_value(), 'O wins!')

    def test_recognises_draw(self):
        self.play(0, 0, 'X')
        self.play(1, 1, 'O')
        self.play(2, 2, 'X')
        self.play(0, 1, 'O')
        self.play(2, 1, 'X')
        self.play(2, 0, 'O')
        self.play(0, 2, 'X')
        self.play(1, 2, 'O')
        self.play(1, 0, 'X')
        self.assertEqual("It's a draw", self.message_value())

    def check_board(self, expected_board):
        self.assertEqual(self.see_expected_board(expected_board), self.see_board())

    def see_expected_board(self, expected_board):
        result = []
        lines = expected_board.split('\n')
        for line in lines:
            for char in line:
                if char in 'XO':
                    result.append(char)
                if char == '-':
                    result.append(' ')
        return result

    def see_board(self):
        result = []
        for y in range(3):
            for x in range(3):
                result.append(self.app.square(x, y).text)
        return result


