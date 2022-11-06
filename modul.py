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


