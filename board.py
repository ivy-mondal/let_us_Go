# Not so kawaii Go board
from rules import get_board_size
from rules import pass_turn
from rules import get_komi


class Board:
    def __init__(self):
        self.size = get_board_size()
        self.komi = get_komi(self.size)
        self.current_player = 1  # 1 = B
        self.consecutive_passes = 0
        self.board = [[' ' for i in range(self.size)] for _ in range(self.size)]
        self.history = []

    def display(self):
        board_str = "  " + " ".join(chr(65 + i) for i in range(self.size)) + "\n"
        for i, row in enumerate(self.board):
            board_str += f"{i + 1:2d} "
            board_str += " ".join(row) + "\n"

        return board_str

    def handle_pass(self):
        self.consecutive_passes += 1
        return self.consecutive_passes == 2

    def reset_pass(self):
        self.consecutive_passes = 0

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
