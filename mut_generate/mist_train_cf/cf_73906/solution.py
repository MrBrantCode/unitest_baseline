"""
QUESTION:
Create a function `create_df(nrows, ncols)` that instantiates a Pandas dataframe without setting any particular column labels or data instances. The function should handle erroneous inputs robustly by returning a suitable error message when attempted with invalid ones. The function should consider the following restrictions and error cases: 
- Inputs `nrows` and `ncols` cannot be `None`.
- Inputs `nrows` and `ncols` should be integers.
- Number of rows and columns cannot be negative.
- Number of rows and columns cannot exceed a certain threshold (e.g., 10000).
- The function should log error messages into a log file in case of any exceptions.
"""

import pandas as pd
import logging

# Set up logging to file
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='error_log.txt',
                    filemode='w')

def create_df(nrows, ncols):
    if nrows is None or ncols is None:
        logging.error("Error: Input values cannot be None!")
        return "Error: Input values cannot be None!"
    elif not isinstance(nrows, int) or not isinstance(ncols, int):
        logging.error("Error: Input values should be integers!")
        return "Error: Inputs values should be integers!"
    elif nrows < 0 or ncols < 0:
        logging.error("Error: Number of rows and columns cannot be negative!")
        return "Error: Number of rows and columns cannot be negative!"
    elif nrows > 10000 or ncols > 10000: 
        logging.error("Error: Number of rows or columns exceeds the limit!")
        return "Error: Number of rows or columns exceeds the limit!"
    else:
        try:
            df = pd.DataFrame(index=range(nrows), columns = range(ncols))
            return df
        except Exception as e: 
            logging.error("Error: {0}".format(str(e)))
            return "Error: {0}".format(str(e))