import random


def random_state() -> list:
    status = [[], [], []]
    for i in range(3):
        for j in range(3):
            status[i].append(random.randint(0, 2))
    return status


def row_to_str(status: list, flag: bool) -> str:
    status_str = str()
    mapping = {0: ' ', 1: "X", 2: "0"}
    for i in range(3):
        a = ' ' if flag else '_'
        status_str += a + (str(mapping[status[i]]) if status[i] != 0 else a) + (a + '|' if i != 2 else a)
    return status_str


def status_to_str2(status: list) -> str:
    str1 = row_to_str(status[0], False)
    str2 = row_to_str(status[1], False)
    str3 = row_to_str(status[2], True)
    return f"{str1}\n{str2}\n{str3}"


def end_game(value:str):
    if not value:
        print('Игра окончена')
        exit()


def zone_selection(status) -> str:
    index = input('Введите зону ')
    end_game(index)
    while not index.isdigit() or int(index) > 33 or int(index) < 11 or int(index[1]) > 3 or \
            status[int(index[0]) - 1][
                int(index[1]) - 1] != 0:
        index = input('Вы ввели не верную зону\nВведите зону ')
        end_game(index)
    return index


def value_selection()->str:
    elem = input('Введите значение ').upper()
    end_game(elem)
    while elem != 'X' and elem != 'O':
        elem = input('Вы ввели не верное значение\nВведите значение ').upper()
        end_game(elem)
    return elem


def the_game(status: list):
    status_list = [0]
    player = 0
    while status_list.count(0) != 0:
        print()
        print(status_to_str2(status))
        print()
        status_list.clear()
        print('Игрок {}'.format(player % 2 + 1))
        index = zone_selection(status)
        elem = value_selection()
        status[int(index[0]) - 1][int(index[1]) - 1] = 1 if elem == 'X' else 2
        for i in range(3):
            for j in range(3):
                status_list.append(status[i][j])
        player += 1
    print('Игра окончена')
