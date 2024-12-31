from random import randint


def rand_sel(array: list) -> str:
    if len(array) < 10:
        result = str(randint(1, len(array)))
    else:
        result = str(randint(1, 9))
    return result
