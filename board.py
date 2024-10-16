# Not so kawaii Go board
from main import get_board_size


class Board:
    def __init__(self, komi):
        self.size = get_board_size()
        self.komi = komi
        self.current_player = "B"
        self.board = [[' ' for i in range(self.size)] for _ in range(self.size)]
        self.history = []

    def display(self):
        board_str = "  " + " ".join(chr(65 + i) for i in range(self.size)) + "\n"
        for i, row in enumerate(self.board):
            board_str += f"{i + 1:2d} "
            board_str += " ".join(row) + "\n"

        return board_str

    def is_move_legal(self):
        pass

    def make_move(self):
        pass


