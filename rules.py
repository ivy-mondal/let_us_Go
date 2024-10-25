# Play by da rules ;)
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
def check_spot(board, row, col):
    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        return board[row][col] == " "
    return False


# pass logic
def pass_turn(player):
    print(f"Player {player} has decided to embrace the void and paws their turn")
    return "pass"
