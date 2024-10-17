# Play by da rules ;)
# for switching
def switch_player(current_player):  #1=B
    return "2" if current_player == "1" else "1"


# for occupying spot
def check_spot(board, row, col):
    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        return board[row][col] == " "
    return False


# pass logic
def pass_turn(player):
    print(f"Player {player} has decided to embrace the void and pass their turn")
    return "pass"
