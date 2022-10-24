import random


def random_state() -> list:
    status = [[], [], []]
    for i in range(3):
        for j in range(3):
            status[i].append(random.randint(0, 2))
            if status[i][j] == 0 and i != 2:
                status[i].pop(j)
                status[i].append('___')
            elif status[i][j] == 1 and i != 2:
                status[i].pop(j)
                status[i].append('_X_')
            elif status[i][j] == 2 and i != 2:
                status[i].pop(j)
                status[i].append('_O_')
            if status[i][j] == 0 and i == 2:
                status[i].pop(j)
                status[i].append('   ')
            elif status[i][j] == 1 and i == 2:
                status[i].pop(j)
                status[i].append(' X ')
            elif status[i][j] == 2 and i == 2:
                status[i].pop(j)
                status[i].append(' O ')
    return status


def print_matrix(status: list):
    for value in status:
        print('{}|{}|{}'.format(value[0], value[1], value[2]))
