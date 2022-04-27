#!/usr/bin/env python3
from typing import List

from guizero import App, Box, PushButton, Text


class TicTacToeApp(App):
    WINNING_LINES = [
        # Vertical lines
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        # Horizontal lines
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),
        # Diagonals
        ((0, 0), (1, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0))
    ]
    def __init__(self):
        App.__init__(self, "Tic tac toe")
        self.current_player = 'X'
        self.winner = None
        self.board = Box(self, layout="grid")
        self.board_squares = self.clear_board() # List[ist[PushButton]]
        self.message = Text(self, text="It is your turn, " + self.current_player)

    def square(self, x, y) -> PushButton:
        return self.board_squares[x][y]

    def clear_board(self) -> List[List[PushButton]]:
        return [[PushButton(self.board, text=" ", grid=[x, y], width=3, command=self.player_chooses_square, args=[x, y])
                for y in range(3)]
                    for x in range(3)]

    def reset_board(self):
        for x in range(3):
            for y in range(3):
                self.square(x, y).text = " "
                self.square(x, y).enable()
        self.winner = None
        self.current_player = 'X'
        self.message.value = 'It is your turn, X'

    def toggle_player(self):
        self.current_player = 'XO'[self.odd_move()]
        self.message.value = "It is your turn, %s" % self.current_player

    def odd_move(self):
        return self.moves_taken() % 2

    def last_player(self):
        return 'XO'[self.even_move()]

    def even_move(self):
        return not self.odd_move()

    def moves_taken(self):
        return sum(square.text in "XO" for row in self.board_squares for square in row)

    def player_chooses_square(self, x, y):
        self.square(x, y).text = self.current_player
        self.square(x, y).disable()
        self.toggle_player()
        self.is_game_won_or_drawn()

    def line_wins(self, last_player, locations):
        for x, y in locations:
            if self.square(x, y).text != last_player:
                return False
        return True

    def is_game_won_or_drawn(self):
        last_player = self.last_player()
        for line in self.WINNING_LINES:
            if self.line_wins(last_player, line):
                self.game_won_by(last_player)
                return
        if self.game_is_drawn():
            self.message.value = "It's a draw"

    def game_is_drawn(self):
        return self.moves_taken() == 9

    def game_won_by(self, last_player):
        self.winner = last_player
        self.disable_all_squares()
        self.message.value = "%s wins!" % self.winner

    def disable_all_squares(self):
        for i in range(3):
            for j in range(3):
                self.square(i, j).disable()


if __name__ == "__main__":  # pragma no cover
    app = TicTacToeApp()
    app.display()
