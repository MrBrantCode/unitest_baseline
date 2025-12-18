"""
QUESTION:
In the popular spreadsheets systems (for example, in Excel) the following numeration of columns is used. The first column has number A, the second — number B, etc. till column 26 that is marked by Z. Then there are two-letter numbers: column 27 has number AA, 28 — AB, column 52 is marked by AZ. After ZZ there follow three-letter numbers, etc.

The rows are marked by integer numbers starting with 1. The cell name is the concatenation of the column and the row numbers. For example, BC23 is the name for the cell that is in column 55, row 23. 

Sometimes another numeration system is used: RXCY, where X and Y are integer numbers, showing the column and the row numbers respectfully. For instance, R23C55 is the cell from the previous example.

Your task is to write a program that reads the given sequence of cell coordinates and produce each item written according to the rules of another numeration system.

Input

The first line of the input contains integer number n (1 ≤ n ≤ 105), the number of coordinates in the test. Then there follow n lines, each of them contains coordinates. All the coordinates are correct, there are no cells with the column and/or the row numbers larger than 106 .

Output

Write n lines, each line should contain a cell coordinates in the other numeration system.

Examples

Input

2
R23C55
BC23


Output

BC23
R23C55
"""

import re

def convert_cell_notation(cell_notation: str) -> str:
    """
    Converts cell notation between "RXCY" and "Excel" column-row formats.

    :param cell_notation: The input cell notation to be converted.
    :return: The converted cell notation in the opposite format.
    """
    
    def from_excel(item):
        row = ''.join([s for s in item if s.isdigit()])
        column = excel_to_column(item.replace(row, ''))
        return 'R{0}C{1}'.format(row, column)

    def to_excel(item):
        (row, column) = item.split('C')
        (row, column) = (int(row.replace('R', '')), int(column))
        column = column_to_excel(column)
        return '{0}{1}'.format(column, row)

    def column_to_excel(column):
        column = int(column)
        excel_col = str()
        div = column
        while div:
            (div, mod) = divmod(div - 1, 26)
            excel_col = chr(mod + 65) + excel_col
        return excel_col

    def excel_to_column(column):
        expn = 0
        col_num = 0
        for char in reversed(column):
            col_num += (ord(char) - ord('A') + 1) * 26 ** expn
            expn += 1
        return col_num

    def get_type(address):
        if 'R' and 'C' in address and re.match(r'\w{1}\d+\w{1}\d+', address):
            return 1
        return 0

    registry = {0: from_excel, 1: to_excel}
    return registry[get_type(cell_notation)](cell_notation)