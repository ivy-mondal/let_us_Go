# Get my beautiful beautiful board here :)
from board import Board
from rules import pass_turn, simulate_move, check_spot
from rules import switch_player


def main():
    board = Board()
    current_player = 1  # 1=B

    while True:
        move = input(f"Player{current_player}, enter yo move. [(row col) or pass]:")
        if move.lower() == "pass":
            pass_turn(current_player)
            if board.handle_pass():
                print("Both players have raised their paws, Game Ovah!")
                break
        else:
            if check_spot(board, move):
                future_board = simulate_move(board.matrix, move, current_player)
                # move legal
                # make move
                # show board
                board.reset_pass()
                current_player = switch_player(current_player)
            else:
                continue



main()
