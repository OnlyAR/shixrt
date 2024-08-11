from pathlib import Path

import numpy as np


def output(filepath: Path, x: np.ndarray):
    with open(filepath, 'w') as f:
        for x_item in x:
            f.write(f"{x_item}\n")
