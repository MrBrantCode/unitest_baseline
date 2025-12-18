"""
QUESTION:
Write a SQL query to retrieve distinct job titles from an "employees" table. The query should return job titles with 5 or more employees, sorted in descending order by the number of employees with each title.
"""

import pandas as pd

def get_common_job_titles(df):
    return df['job_title'].value_counts()[lambda x: x >= 5].sort_values(ascending=False)