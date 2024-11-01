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
            continue


# for switching
def switch_player(current_player):
    return "B" if current_player == "W" else "W"


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
        if 0 <= row < board.size and 0 <= col < board.size:
            return board.matrix[row][col] == " "
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


# to find connected groups
def find_groups(current_matrix, player_color):
    visited = set()
    groups = []
    size = len(current_matrix)

    def dfs(row, col):
        if not (0 <= row < size and 0 <= col < size):
            return
        if (row, col) in visited or current_matrix[row][col] != player_color:
            return
        visited.add((row, col))
        current_group.append((row, col))

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for x, y in directions:
            dfs(row + x, col + y)

    for row in range(size):
        for col in range(size):
            if current_matrix[row][col] == player_color and (row, col) not in visited:
                current_group = []
                dfs(row, col)
                if current_group:
                    groups.append(current_group)
    return groups


# Crystal ball for Go
def simulate_move(board_matrix, move, current_player):
    row, col = map(int, move.split())
    current_matrix = copy.deepcopy(board_matrix)
    current_matrix[row][col] = current_player
