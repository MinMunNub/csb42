map = [
["p","-","-","-","-"],
["-","-","k","-","-"],
["-","-","-","-","-"],
["d","-","-","-","-"]
]

player_x = 0
player_y = 0
has_key = False


def show_map():
    for row in map:
        for cell in row:
            print(cell,end=" ")
        print()


while True:

    show_map()

    move = input("move w a s d ")

    map[player_y][player_x] = "-"

    if move == "w":
        player_y -= 1
    if move == "s":
        player_y += 1
    if move == "a":
        player_x -= 1
    if move == "d":
        player_x += 1

    if map[player_y][player_x] == "k":
        has_key = True
        print("you got the key")

    if map[player_y][player_x] == "d":
        if has_key:
            print("you win")
        else:
            print("you lose need key")
        break

    map[player_y][player_x] = "p"