"""
QUESTION:
Construct a function `detailed_levenshtein(a, b)` that calculates the Levenshtein distance between two input strings `a` and `b` and provides a detailed analysis of the operations executed, including the count of each operation (inclusion, removal, and replacement) and the specific location in the string where they were implemented. The function should be able to process both standard English alphabets and non-English alphabets encompassing Unicode characters.
"""

def levenshtein(a, b):
    chars_a = list(a)
    chars_b = list(b)
    num_rows = len(chars_a) + 1
    num_cols = len(chars_b) + 1

    operations = [[[] for j in range(num_cols)] for i in range(num_rows)]
    costs = [[0 for j in range(num_cols)] for i in range(num_rows)]
    for i in range(num_rows):
        costs[i][0] = i
        if i > 0:
            operations[i][0] = [('delete', chars_a[i - 1], i - 1)]
    for j in range(num_cols):
        costs[0][j] = j
        if j > 0:
            operations[0][j] = [('insert', chars_b[j - 1], j - 1)]
    for i in range(1, num_rows):
        for j in range(1, num_cols):
            del_op = ('delete', chars_a[i - 1], i - 1)
            ins_op = ('insert', chars_b[j - 1], j - 1)
            if chars_a[i - 1] == chars_b[j - 1]:
                sub_op = ('keep', chars_a[i - 1], i - 1)
                sub_cost = costs[i - 1][j - 1]
            else:
                sub_op = ('replace', (chars_a[i - 1], chars_b[j - 1]), (i - 1, j - 1))
                sub_cost = costs[i - 1][j - 1] + 1
            del_cost = costs[i - 1][j] + 1
            ins_cost = costs[i][j - 1] + 1
            costs[i][j], operations[i][j] = min((del_cost, operations[i - 1][j] + [del_op]),
                                                 (ins_cost, operations[i][j - 1] + [ins_op]),
                                                 (sub_cost, operations[i - 1][j - 1] + [sub_op]))

    return (costs[-1][-1], operations[-1][-1])