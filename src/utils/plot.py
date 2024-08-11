from typing import Union, List

import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', family='Times New Roman')
plt.rc('font', size=30)


def plot_original(x: Union[np.ndarray, List]):
    plt.figure(figsize=(16, 8))
    t = np.arange(len(x))
    plt.scatter(t, x, s=5, marker='o')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()
    plt.close()


def plot_result(x: Union[np.ndarray, List],
                gold: Union[np.ndarray, List],
                pred: Union[np.ndarray, List] = None):
    plt.figure(figsize=(16, 8))
    plt.scatter(np.arange(len(gold)), gold, s=100, marker='o', c='r', label='Gold')
    # plt.plot(gold, ls="--", c='r')
    if pred is not None:
        plt.scatter(np.arange(len(pred)), pred, s=50, marker='o', c='g', label='Predicted')
    plt.grid(axis='y')
    plt.xticks(np.arange(len(gold)), np.arange(len(x), len(x) + len(gold), 1))
    plt.legend(['Gold', 'Predicted'])
    plt.tight_layout()
    plt.show()
    plt.close()
