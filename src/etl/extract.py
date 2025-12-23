import pandas as pd

def extract(file_path):
    df = pd.read_csv(file_path)
    return df
