# Get my beautiful beautiful board here :)
from board import Board
from rules import pass_turn, simulate_move, check_spot
from rules import switch_player


def main():
    board = Board()

    while True:
        print(board.display())
        move = input(f"Player{board.current_player}, enter yo move. [(row col) or pass]:")
        if board.is_move_legal(move):
            board.make_move(move)
        else:
            print("Move illegal")

        if board.is_game_over():
            print("Both players have raised their paws, Game Ovah!")

            print("Score", board.get_score())
            break;


main()