"""
QUESTION:
Write a function named `test_lazy_tables` that uses the pytest framework to test the presence of a specific table in a list of support tables. The function should be parameterized to test for the "ANTENNA" table. The list of support tables should be provided as a fixture. The function should assert that the "ANTENNA" table is present in the list of support tables.
"""

def entrance(support_tables, table):
    return table in support_tables