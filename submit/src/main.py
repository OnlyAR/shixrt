from fourier.workflow import fourier_fit

if __name__ == '__main__':
    # tag = "2-2"
    # data_dir = Path(__file__).parent.parent / 'data' / 'problem1'
    #
    # input_filename = data_dir / f"data{tag}.csv"
    # gold_filename = data_dir / f"gold{tag}.csv"
    # output_filename = data_dir / f"result{tag}.csv"

    input_file = "data1.csv"
    output_file = f"result1.csv"
    fourier_fit(input_file=input_file, output_file=output_file)
    # evaluate(output_file=output_filename, gold_file=gold_filename)
