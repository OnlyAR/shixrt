from typing import List

import numpy as np


class Fourier:
    def __init__(
            self,
            time_series: np.ndarray,
            x_off: int,
            t: int,
            terms: int = 0,
            end: int = 5000,
            step: int = 100,
            error=1e-5
    ):
        self.a0: float = 0
        self.a: List = []
        self.b: List = []
        self.x_off = x_off
        self.t = t
        self.time_series = time_series[x_off: x_off + t]
        self.x = np.arange(t)
        self.terms = terms
        self.end = end
        self.step = step
        self.error = error
        print("Initialized {}".format(self))
        self._fit()

    def _rollback(self):
        self.terms -= self.step
        self.a = self.a[:self.terms]
        self.b = self.b[:self.terms]

    def _fit(self):
        print("Fitting Fourier model...")
        self.a0 = self.compute_a0()

        if self.terms > 0:
            print("Terms set to {}, computing coefficients...", self.terms)
            self.a = [self.compute_an(i + 1) for i in range(self.terms)]
            self.b = [self.compute_bn(i + 1) for i in range(self.terms)]
            error = self.eval(len(self.time_series) // 10)
            print(f"Terms: {self.terms}, error: {error}")
        else:
            prev_error = None
            print("Terms not set, computing coefficients until error < {}".format(self.error))
            while self.terms < self.end:
                self.a += [self.compute_an(i + 1) for i in range(self.terms, self.terms + self.step)]
                self.b += [self.compute_bn(i + 1) for i in range(self.terms, self.terms + self.step)]
                self.terms += self.step
                error = self.eval(len(self.time_series) // 100)
                print(f"Terms: {self.terms}, error: {error}")
                if error < self.error:
                    break
                if prev_error and error > prev_error:
                    print("Error increased, breaking")
                    self._rollback()
                    break
                prev_error = error
            if self.terms >= self.end:
                print("Reached maximum terms without convergence")
        print("Fitted Fourier model with {} terms".format(self.terms))

    def compute_a0(self):
        return np.mean(self.time_series[:self.t])

    def compute_an(self, n: int):
        cos_term = np.cos(2 * np.pi * n * self.x / self.t)
        product = self.time_series * cos_term
        sum_product = np.sum(product)
        coefficient = sum_product * 2 / self.t
        return coefficient

    def compute_bn(self, n: int):
        sin_term = np.sin(2 * np.pi * n * self.x / self.t)
        product = self.time_series * sin_term
        sum_product = np.sum(product)
        coefficient = sum_product * 2 / self.t
        return coefficient

    def predict(self, x: float):
        x = x - self.x_off
        y = self.a0
        y += sum(self.a[i] * np.cos(2 * np.pi * (i + 1) * x / self.t) for i in range(self.terms))
        y += sum(self.b[i] * np.sin(2 * np.pi * (i + 1) * x / self.t) for i in range(self.terms))
        return y

    def eval(self, sample_num):
        sample = np.linspace(0, self.t, sample_num, endpoint=False, dtype=int)
        y = self.time_series[sample]
        y_hat = [self.predict(i) for i in sample]
        error = np.mean(np.abs(y - y_hat))
        return error

    def __str__(self):
        template = "{k}={v}"
        info_list = [template.format(k="time_series_length", v=len(self.time_series))]
        for k in ("terms", "end", "step", "error"):
            info_list.append(template.format(k=k, v=getattr(self, k)))

        return "Fourier({})".format(", ".join(info_list))
