"""
QUESTION:
Write a function `filter_emails` that extracts email addresses commencing with the letter "p" from a given dataframe or SQL table "users". The function should return a dataframe containing only the rows where the email starts with 'p'. The function should work with both pandas dataframe and SQL table as input.
"""

import pandas as pd
import sqlite3

def filter_emails(df_or_conn, table_name='users'):
    """
    Extract email addresses commencing with the letter "p" from a given dataframe or SQL table.
    
    Parameters:
    df_or_conn (pd.DataFrame or sqlite3.Connection): The input dataframe or SQL connection.
    table_name (str): The name of the SQL table (default is 'users').
    
    Returns:
    pd.DataFrame: A dataframe containing only the rows where the email starts with 'p'.
    """
    
    if isinstance(df_or_conn, pd.DataFrame):
        df = df_or_conn
    else:
        df = pd.read_sql_query(f"SELECT * from {table_name}", df_or_conn)
    
    df['email'] = df['email'].astype(str)
    return df[df['email'].str.startswith('p')]