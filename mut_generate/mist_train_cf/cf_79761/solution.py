"""
QUESTION:
Write a SQL script that can call other SQL scripts from different directories using the \i command, without encountering a "Permission denied" error. The script should work on Windows using Postgres Plus 8.3 and the default postgres user.
"""

def entance(s):
    return s.replace('\\', '/') if '\\' in s else s.replace('/', '\\')