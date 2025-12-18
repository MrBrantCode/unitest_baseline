"""
QUESTION:
Create a function `custom_sort(records)` that takes a list of financial records as input, where each record is a dictionary containing a 'fiscal_year' key. The function should return a new list of records sorted in ascending order by 'fiscal_year', but with all leap years placed at the end. A year is considered a leap year if it is divisible by 4, except for end-of-century years which must be divisible by 400.
"""

def custom_sort(records):
    leap_year_records = [record for record in records if (record['fiscal_year'] % 4 == 0 and (record['fiscal_year'] % 100 != 0 or record['fiscal_year'] % 400 == 0))]
    non_leap_year_records = [record for record in records if not (record['fiscal_year'] % 4 == 0 and (record['fiscal_year'] % 100 != 0 or record['fiscal_year'] % 400 == 0))]
    
    return sorted(non_leap_year_records, key=lambda x: x['fiscal_year']) + sorted(leap_year_records, key=lambda x: x['fiscal_year'])