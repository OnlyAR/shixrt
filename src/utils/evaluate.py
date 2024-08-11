from pathlib import Path

import numpy as np

from utils.dataloader import DataLoader
from utils.plot import plot_result


def evaluate(input_file: Path, output_file: Path, gold_file: Path):
    origin = DataLoader.load_data(input_file)
    gold = DataLoader.load_data(gold_file)
    with open(output_file, 'r') as f:
        out = np.array([float(l) for l in f.readlines()])

    error = np.mean(np.abs(gold - out))
    x = np.arange(len(gold))
    # plot_result(x, gold, out)
    plot_result(origin, gold, out)
    print(error)
