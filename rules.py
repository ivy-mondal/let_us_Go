# Play by da rules ;)
import copy


# board size
def get_board_size():
    while True:
        n = input("Choose board size, 9,13 or 19:")
        if n in ["9", "13", "19"]:
            return int(n)
        else:
            print("🤨😑" + "\nIf you want to play give correct board size 🙂")


# for switching
def switch_player(current_player):  # 1=B
    return 3 - current_player


# get komi
def get_komi(board_size):
    if board_size == 9:
        return 7.5
    elif board_size == 13:
        return 7.5
    elif board_size == 19:
        return 7.5


# for occupying spot
def check_spot(board, move):
    try:
        row, col = map(int, move.split())
        if 0 <= row < len(board) and 0 <= col < len(board[0]):
            return board[row][col] == " "
        else:
            print("Check your coordinates and try again! 😭")
            return False
    except ValueError:
        print("Please stick to correct format, only numbers allowed 🧐")
        return False


# pass logic
def pass_turn(player):
    print(f"Player {player} has decided to embrace the void and extend paws in their turn")
    return "pass"


# Crystal ball for Go
def simulate_move(board_matrix, move, current_player):
    row, col = map(int, move.split())
    current_matrix = copy.deepcopy(board_matrix)
    if current_matrix[row][col] is None:
        # logic is coming hold on
        pass
