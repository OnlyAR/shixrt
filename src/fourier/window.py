import numpy as np


def sim(x: np.ndarray, y: np.ndarray) -> float:
    return np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))


def sliding_window(time_series) -> int:
    length = len(time_series)
    delta_y = np.max(time_series) - np.min(time_series)
    window = length // 2
    sim_dict = {}
    while window > 1:
        left = length - 2 * window
        mid = window
        t1 = time_series[left:left + mid]
        t2 = time_series[left + mid:]
        if np.max(t2) - np.min(t2) < 0.8 * delta_y:
            break
        cur_sim = sim(t1, t2)
        sim_dict[window] = cur_sim
        window -= 1

    return max(sim_dict, key=sim_dict.get)
