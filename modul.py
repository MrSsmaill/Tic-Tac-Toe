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
    # rez = [mapping[k[k]] for k in range(3)]
    for i in range(3):
        if flag:
            status_str += ' ' + str(mapping[status[i]]) + (' |' if i != 2 else ' ')
        else:
            status_str += '_' + (str(mapping[status[i]]) if status[i] != 0 else '_') + ('_|' if i != 2 else '_')
    return status_str


def status_to_str2(status: list) -> str:
    str1 = row_to_str(status[0], False)
    str2 = row_to_str(status[1], False)
    str3 = row_to_str(status[2], True)
    return f"{str1}\n{str2}\n{str3}"


def status_to_str(status: list) -> str:
    status_str = str()
    for i in range(3):
        for j in range(3):
            if i != 2:
                a = '_'
            else:
                a = ' '
            if status[i][j] == 0 and i != 2:
                status_str += a + '_' + a
            elif status[i][j] == 1:
                status_str += a + 'X' + a
            elif status[i][j] == 2:
                status_str += a + 'O' + a
            elif status[i][j] == 0 and i == 2:
                status_str += a + ' ' + a
            if j == 2:
                status_str += '\n'
            else:
                status_str += '|'

    return status_str


def print_matrix(status_str: str):
    print(status_str)
