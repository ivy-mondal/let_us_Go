# Get my beautiful beautiful board here :)
from board import Board
from rules import pass_turn
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
            board.reset_pass()

        current_player = switch_player(current_player)


main()
