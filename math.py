import numpy as np


def round_up(number: float, to_nearest: int = 1):
    return int(np.ceil(number / to_nearest)) * to_nearest


def round_down(number: float, to_nearest: int = 1):
    return int(np.floor(number / to_nearest)) * to_nearest
