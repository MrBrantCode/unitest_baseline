"""
QUESTION:
在 SQLite 中操作一个名为 "dumpling" 的表格，要求表格中每一列都有一定数量（假设为 column_min_count）的数据，并且只有一个线程可以操作该表格。编写一个名为 `check_column_counts` 的函数来检查表格中每一列的数据量是否符合要求，并返回布尔值。 

此函数接受一个 SQLite 游标（cursor）作为参数，并且需要在函数体内使用该游标来执行 SQL 查询。函数不应包含任何其他参数。 

此函数应在找到任意一列数据量不足时立即返回 False，若所有列的数据量都符合要求，则返回 True。
"""

import sqlite3

def check_column_counts(cursor):
    # 获取表格中每一列的名称
    cursor.execute("PRAGMA table_info(dumpling)")
    columns = [column[1] for column in cursor.fetchall()]

    for column in columns:
        # 查询该列的数据量
        cursor.execute(f"SELECT COUNT({column}) FROM dumpling")
        count = cursor.fetchone()[0]

        # 如果数据量不够，返回False
        if count < 10: # column_min_count
            return False

    # 所有列的数据量都符合要求，返回True
    return True