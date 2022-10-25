import random


def random_state() -> list:
    status = [[], [], []]
    for i in range(3):
        for j in range(3):
            status[i].append(random.randint(0, 2))
    return status


def to_str(status: list) -> list:
    status_str = []
    i = 0
    for elem in status:
        for value in elem:
            if value == 0 and i > 5:
                status_str.append(' ')
            elif value == 0:
                status_str.append('_')
            elif value == 1:
                status_str.append('X')
            elif value == 2:
                status_str.append('O')
            i += 1
    return status_str


def print_matrix(status: list):
    i = 0
    while i < len(status):
        if i > 5:
            print(' {} | {} | {} '.format(status[i], status[i + 1], status[i + 2]))
        else:
            print('_{}_|_{}_|_{}_'.format(status[i], status[i + 1], status[i + 2]))
        i += 3
