"""
QUESTION:
Implement a function `parse_command_line_args` that takes a list of command-line arguments and returns a dictionary containing the parsed arguments. The function should handle the following arguments:
- `--classification-type`: Specifies the classification type, either 'binary' or 'multi-class'.
- `--setting-name`: Specifies the setting name.
- `-c` or `--classifier`: Specifies the classifier, with choices 'rf', 'gbdt', or 'mlp'.
- `--testing-time`: Specifies the testing time, a string in the format 'start_time,end_time'.
- `--month-interval`: Specifies the month interval, an integer with a default value of 1.

The returned dictionary should contain the following keys and corresponding values:
- 'classification_type': The specified classification type.
- 'setting_name': The specified setting name.
- 'classifier': The specified classifier.
- 'testing_time': A tuple containing the start and end times for testing.
- 'month_interval': The specified month interval.

The function should handle any missing arguments or invalid choices and provide appropriate error messages.
"""

from typing import List, Dict, Union, Tuple
import argparse

def parse_command_line_args(args: List[str]) -> Dict[str, Union[str, Tuple[str, str], int]]:
    parser = argparse.ArgumentParser(description='Machine Learning Model CLI')
    parser.add_argument('--classification-type', required=True, choices=['binary', 'multi-class'], help='Whether to perform binary classification or multi-class classification.')
    parser.add_argument('--setting-name', required=True, help='Name for this particular setting, for saving corresponding data, model, and results')
    parser.add_argument('-c', '--classifier', required=True, choices=['rf', 'gbdt', 'mlp'], help='The classifier used for binary classification or multi-class classification')
    parser.add_argument('--testing-time', required=True, help='The beginning time and ending time (separated by comma) for a particular testing set (bluehex data)')
    parser.add_argument('--month-interval', type=int, default=1, help='Specify how many months for sampling.')

    parsed_args = vars(parser.parse_args(args))

    start_time, end_time = parsed_args['testing_time'].split(',')
    parsed_args['testing_time'] = (start_time, end_time)

    return parsed_args