#!/usr/bin/env python3
from guizero import PushButton

def push(button: PushButton) -> None:
    button.tk.invoke()

import unittest
from tictactoe import TicTacToeApp

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.app = TicTacToeApp()

    def setUp(self) -> None:
        self.app.reset_board()

    def message_value(self):
        return self.app.message.value

    def play(self, x, y, player):
        self.assertEqual(self.message_value(), 'It is your turn, %s' % player)
        push(self.app.square(x, y))

    def test_turn_changes_after_player_moves(self):
        self.play(0, 0, 'X')
        self.assertEqual(self.message_value(), 'It is your turn, O')

    # def test_knows_if_x_has_won(self):
    #     self.play(0, 0, 'X')
    #     self.play(0, 1, 'O')
    #     self.play(1, 0, 'X')
    #     self.play(0, 2, 'O')
    #     self.play(2, 0, 'X')
    #     self.check_board("X--OX-O-X")
    #     self.assertEqual(self.message_value(), 'X wins!')

    def test_knows_if_o_has_won(self):
        self.play(0, 0, 'X')
        self.check_board("X-- --- ---")
        self.play(0, 1, 'O')
        self.check_board("X-- O-- ---")
        self.play(1, 0, 'X')
        self.check_board("XX- O-- ---")
        self.play(1, 1, 'O')
        self.check_board("XX- OO- ---")
        self.play(1, 2, 'X')
        self.check_board("XX- OO- -X-")
        self.play(2, 1, 'O')
        self.check_board("XX- OO0 -X-")
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
        return list(row[0] for row in zip(expected_board.split(' ')))

    def see_board(self):
        result = []
        for y in range(3):
            row = ''
            for x in range(3):
                row += self.square_contents(x, y)
            result.append(row)
        return result

    def square_contents(self, x, y):
        return self.app.square(x, y).text.replace(' ','-')


