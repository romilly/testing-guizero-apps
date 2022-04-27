#!/usr/bin/env python3
from guizero import App, Box, PushButton, Text


class TicTacToeApp(App):
    def __init__(self):
        App.__init__(self, "Tic tac toe")
        self.turn = 'X'
        self.winner = None
        self.board = Box(self, layout="grid")
        self.board_squares = self.clear_board()
        self.message = Text(self, text="It is your turn, " + self.turn)
        self.winning_lines = [
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

    def square(self, x, y):
        return self.board_squares[x][y]

    def clear_board(self):
        new_board = [[None, None, None], [None, None, None], [None, None, None]]
        for x in range(3):
            for y in range(3):
                button = PushButton(self.board, text=" ", grid=[x, y], width=3, command=self.choose_square, args=[x, y])
                new_board[x][y] = button
        return new_board

    def reset_board(self):
        for x in range(3):
            for y in range(3):
                self.square(x, y).text = " "
                self.square(x, y).enable()
        self.winner = None
        self.turn = 'X'
        self.message.value = 'It is your turn, X'

    def toggle_player(self):
        self.turn = 'XO'[1 == self.moves_taken() % 2]
        self.message.value = "It is your turn, %s" % self.turn

    def last_player(self):
        return 'XO'[0 == self.moves_taken() % 2]

    def moves_taken(self):
        return sum(square.text in "XO" for row in self.board_squares for square in row)

    def choose_square(self, x, y):
        self.square(x, y).text = self.turn
        self.square(x, y).disable()
        self.toggle_player()
        self.is_game_won_or_drawn()

    def winning_line(self, last_player, locations):
        for x, y in locations:
            if self.square(x, y).text != last_player:
                return False
        return True

    def is_game_won_or_drawn(self):
        last_player = self.last_player()
        for line in self.winning_lines:
            if self.winning_line(last_player, line):
                self.winner = last_player
                self.disable_all_squares()
                self.message.value = "%s wins!" % self.winner
                return
        if self.moves_taken() == 9:
            self.message.value = "It's a draw"

    def disable_all_squares(self):
        for i in range(3):
            for j in range(3):
                self.square(i, j).disable()


if __name__ == "__main__":  # pragma no cover
    app = TicTacToeApp()
    app.display()
