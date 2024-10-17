# Get my beautiful beautiful board here :)


def get_board_size():
    while True:
        n = input("Choose board size, 9,13 or 19:")
        if n in ["9", "13", "19"]:
            return int(n)
        else:
            print("🤨😑" + "\nIf you want to play give correct board size 🙂")

current_player = 1 #1=B
while True:
    if move == make_move