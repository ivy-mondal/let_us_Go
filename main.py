# Get my beautiful beautiful board here :)
from board import Board
from rules import pass_turn, simulate_move, check_spot
from rules import switch_player


def main():
    board = Board()
    game_over = False  # 1=B

    while not game_over:
        move = input(f"Player{board.current_player}, enter yo move. [(row col) or pass]:")






main()
