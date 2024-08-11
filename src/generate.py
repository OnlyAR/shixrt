import sys
from pathlib import Path

import numpy as np
from utils.plot import plot_result


def func(t):
    base_feq = 18000
    x = np.sin(2 * np.pi * t / base_feq) + np.sin(2 * np.pi * t / (base_feq / 3))
    return x


if __name__ == '__main__':
    t = np.arange(0, 72000, 1)
    x = func(t)
    data_dir = Path(__file__).parent.parent

    train_data = x[:-10] + np.random.normal(0, 0.1, len(x) - 10)
    plot_result(t[:-10], train_data)
    gold_data = x[-10:]

    with open(data_dir / "data1.csv", 'w') as f:
        for idx, x_item in enumerate(train_data):
            f.write(f"{idx},{x_item}\n")

    x = func(t)
    with open(data_dir / "gold1.csv", 'w') as f:
        for idx, x_item in enumerate(gold_data):
            f.write(f"{idx + len(train_data)},{x_item}\n")
    print("Done")
