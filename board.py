# Not so kawaii Go board
from main import get_board_size
from rules import pass_turn


class Board:
    def __init__(self, komi):
        self.size = get_board_size()
        self.komi = komi
        self.current_player = "1"  #1 = B
        self.consecutive_passes = 0
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
        while True:
            move = input(f"Player {self.current_player}, enter your move [(row col) or pass]:")
            if move.lower() == "pass":
                self.consecutive_passes += 1
                return pass_turn(self.current_player)
            else:
                self.consecutive_passes = 0



