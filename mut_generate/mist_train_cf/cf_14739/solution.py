"""
QUESTION:
Write a function, `get_active_users`, to retrieve a list of usernames of users who have more than 5 posts and their account has been active for at least 6 months. The function should query a database with 'users' and 'posts' tables where 'users' table has columns 'id' and 'username', and 'posts' table has columns 'id', 'user_id', and 'created_date'.
"""

import sqlite3
from datetime import datetime, timedelta

def get_active_users(conn):
    cur = conn.cursor()
    six_months_ago = (datetime.now() - timedelta(days=183)).strftime('%Y-%m-%d')
    cur.execute("""
        SELECT users.username
        FROM users
        JOIN posts ON users.id = posts.user_id
        WHERE posts.created_date >= ?
        GROUP BY users.username
        HAVING COUNT(posts.id) > 5
    """, (six_months_ago,))
    return cur.fetchall()