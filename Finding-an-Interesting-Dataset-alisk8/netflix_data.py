import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

netflix_data = pandas.read_csv(
    r"C:/Users/alish/OneDrive/Desktop/HTH_build_sumer_2022/Finding-an-Interesting-Dataset-alisk8/titles.csv")

print(netflix_data)
