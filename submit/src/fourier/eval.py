import numpy as np


def evaluate(pred: np.ndarray, gold: np.ndarray) -> float:
    return 1 - float(np.mean(np.abs(pred - gold) / np.abs(gold)))
