"""
QUESTION:
Your task is to develop a tiny little part of spreadsheet software.

Write a program which adds up columns and rows of given table as shown in the following figure:

<image>



Input

The input consists of several datasets. Each dataset consists of:


n (the size of row and column of the given table)
1st row of the table
2nd row of the table
:
:
nth row of the table


The input ends with a line consisting of a single 0.

Output

For each dataset, print the table with sums of rows and columns. Each item of the table should be aligned to the right with a margin for five digits. Please see the sample output for details.

Example

Input

4
52 96 15 20
86 22 35 45
45 78 54 36
16 86 74 55
4
52 96 15 20
86 22 35 45
45 78 54 36
16 86 74 55
0


Output

52   96   15   20  183
   86   22   35   45  188
   45   78   54   36  213
   16   86   74   55  231
  199  282  178  156  815
   52   96   15   20  183
   86   22   35   45  188
   45   78   54   36  213
   16   86   74   55  231
  199  282  178  156  815
"""

def calculate_spreadsheet_sums(n, table):
    # Calculate row sums and append them to each row
    for row in table:
        row.append(sum(row))
    
    # Calculate column sums
    sum_lst = []
    for i in range(len(table[0])):
        s = 0
        for j in range(n):
            s += table[j][i]
        sum_lst.append(s)
    
    # Append the column sums to the table
    table.append(sum_lst)
    
    return table