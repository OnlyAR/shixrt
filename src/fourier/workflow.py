import sys
from pathlib import Path

import numpy as np

from utils.dataloader import DataLoader
from fourier.filter import filter_signal, smooth_answer
from fourier.fourier import Fourier
from fourier.output import output
from fourier.window import sliding_window
from fourier.offset import y_offset, x_offset

from utils.plot import plot_original


def fourier_fit(input_file: Path, output_file: Path):
    dataloader = DataLoader(input_file)
    time_series = dataloader.time_series

    plot_original(time_series)

    filtered_time_series = filter_signal(time_series, sigma=100)
    y_off = y_offset(filtered_time_series)
    t = sliding_window(filtered_time_series)

    print("t:", t)

    x_off = x_offset(filtered_time_series, y_off, t)
    fourier = Fourier(filtered_time_series, x_off=x_off, t=t, error=1e-6)
    x = np.arange(len(time_series))
    pred_idx = np.arange(len(x), len(x) + 10)
    pred = [fourier.predict(i) for i in pred_idx]
    pred = np.array(pred)
    smoothed = smooth_answer(time_series, pred)
    output(output_file, smoothed)
