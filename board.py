# Not so kawaii Go board
from rules import get_board_size, pass_turn, get_komi, check_spot, simulate_move, switch_player


class Board:
    def __init__(self):
        self.size = get_board_size()
        self.komi = get_komi(self.size)
        self.current_player = "B"
        self.consecutive_passes = 0
        self.matrix = [[' ' for i in range(self.size)] for _ in range(self.size)]
        self.history = []

    def display(self):
        board_str = "  " + " ".join(chr(65 + i) for i in range(self.size)) + "\n"
        for i, row in enumerate(self.matrix):
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

    def make_move(self, move):
        if move.lower() == "pass":
            return self.handle_pass()
            if self.handle_pass():
                print("Both players have raised their paws, Game Ovah!")
            else:
                if check_spot(self, move):
                    future_board = simulate_move(self.matrix, move, current_player)
                    # move legal
                    # make move
                    # show board
                    self.reset_pass()
                    current_player = switch_player(current_player)




