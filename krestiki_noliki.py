def start():
    print("Приветствую в игре")


def show():
    print(f"  0 1 2")
    for i, j in enumerate(field):
        print(f"{i} {' '.join(j)}")


def move():
    while True:
        cords = input("Координаты хода: ").split()

        if len(cords) != 2:
            print("Введите правильные координаты")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите правильные координаты")
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Вне координат")
            continue

        if field[x][y] != " ":
            print("Пусто")
            continue

        return x, y


def win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)), ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))

    for cord in win_cord:
        combinate = []

        for c in cord:
            combinate.append(field[c[0]][c[1]])

        if combinate == ["X", "X", "X"]:
            print("Крестики победили")
            return True

        if combinate == ["0", "0", "0"]:
            print("Нолики победили")
            return True
    return False


start()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1

    show()

    if count % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x, y = move()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win():
        break

    if count == 9:
        print("Ничья")
        break
