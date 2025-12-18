"""
QUESTION:
Create a function `reformat_date` that takes two string parameters `src_date` and `tgt_date`. The function should identify the date format of `src_date` (either YYYYMMDD, YYYY-MM-DD, or MM/DD/YYYY) and convert `tgt_date` to the same format as `src_date`. The function should return the converted `tgt_date` in the YYYYMMDD format.
"""

from datetime import datetime

def reformat_date(src_date, tgt_date):
    # Recognize date format
    if "-" in src_date:
        date_format = "%Y-%m-%d"
    elif "/" in src_date:
        date_format = "%m/%d/%Y"
    else:
        date_format = "%Y%m%d"

    # Convert target date to source date format
    converted_date = datetime.strptime(tgt_date, date_format).strftime('%Y%m%d')
    return converted_date