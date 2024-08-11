from pathlib import Path

from fourier.workflow import fourier_fit
from utils.evaluate import evaluate

if __name__ == '__main__':
    tag = "1-3"
    data_dir = Path(__file__).parent.parent / 'data' / 'problem1'

    input_file = data_dir / f"data{tag}.csv"
    gold_file = data_dir / f"gold{tag}.csv"
    output_file = data_dir / f"result{tag}.csv"

    # input_file = "data1.csv"
    # output_file = "result1.csv"
    # gold_file = "gold1.csv"
    fourier_fit(input_file=input_file, output_file=output_file)
    evaluate(input_file=input_file, output_file=output_file, gold_file=gold_file)
