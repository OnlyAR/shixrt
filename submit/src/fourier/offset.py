import numpy as np


def y_offset(time_series: np.ndarray) -> float:
    y_max = np.max(time_series)
    y_min = np.min(time_series)
    return (y_max + y_min) / 2


def x_offset(time_series: np.ndarray, y_off: float, t: int) -> int:
    x_off = 0
    sim_x_off = 0
    sim_abs = 1
    for i in range(t):
        if np.abs(time_series[i] - y_off) < sim_abs:
            sim_x_off = i
            sim_abs = np.abs(time_series[i] - y_off)
        x_off += 1

    return sim_x_off
