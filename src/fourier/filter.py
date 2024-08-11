import numpy as np

from scipy.ndimage import gaussian_filter
from scipy.interpolate import CubicSpline


def filter_signal(time_series: np.ndarray, sigma=1):
    diff_signal = np.diff(time_series)
    threshold = 3 * np.std(diff_signal)
    rough_regions = np.abs(diff_signal) > threshold
    rough_indices = np.where(rough_regions)[0]
    filtered_time_series = gaussian_filter(time_series, sigma=sigma)
    for i in rough_indices:
        begin = max(0, i - sigma)
        end = min(len(time_series), i + sigma)
        time_series[begin:end] = filtered_time_series[begin:end]
    return time_series


def smooth_answer(time_series: np.ndarray, result: np.ndarray):
    tail = time_series[-10:]
    contacted = np.concatenate([tail, result])
    times_points = np.arange(len(contacted))
    cs = CubicSpline(times_points, contacted)
    return cs(times_points[len(tail):])
