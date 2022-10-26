import random


def random_state() -> list:
    status = [[], [], []]
    for i in range(3):
        for j in range(3):
            status[i].append(random.randint(0, 2))
    return status


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
