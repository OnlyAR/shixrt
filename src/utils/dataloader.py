from pathlib import Path

import numpy as np


class DataLoader:
    def __init__(self, data_path: Path):
        self.data_path = data_path
        self.time_series = self.load_data(data_path)

    @staticmethod
    def load_data(data_path: Path):
        with open(data_path, 'r') as f:
            lines = f.readlines()
        data = []
        for line in lines:
            index, value = line.split(",")
            data.append(value)
        data = np.array(data, dtype=np.float32)
        print(f"Loaded data from {data_path}")
        return data

    def __str__(self):
        return f"DataLoader(data_path={self.data_path})"
