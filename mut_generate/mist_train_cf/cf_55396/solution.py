"""
QUESTION:
Write a Python function `load_dataset` to fine-tune a pre-trained GPT-3 model for text generation using a CSV file. The CSV file must contain a column labeled 'text'. The function should read the text data from the CSV file and return it as a list of strings.

Restrictions:
- The function should take two parameters: `csv_file` (the path to the CSV file) and `text_col` (the column label of the text data, default is 'text').
- The function should use the Pandas library to read the CSV file.
- The function should return a list of strings containing the text data.
- The function will be used to fine-tune a pre-trained GPT-3 model, but this is not part of the function's responsibility.
"""

import pandas as pd

def load_dataset(csv_file, text_col='text'):
    df = pd.read_csv(csv_file)
    text = df[text_col].tolist()
    return text