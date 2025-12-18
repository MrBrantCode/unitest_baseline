"""
QUESTION:
This is yet another problem dealing with regular bracket sequences.

We should remind you that a bracket sequence is called regular, if by inserting «+» and «1» into it we can get a correct mathematical expression. For example, sequences «(())()», «()» and «(()(()))» are regular, while «)(», «(()» and «(()))(» are not. 

You are given a string of «(» and «)» characters. You are to find its longest substring that is a regular bracket sequence. You are to find the number of such substrings as well.

Input

The first line of the input file contains a non-empty string, consisting of «(» and «)» characters. Its length does not exceed 106.

Output

Print the length of the longest substring that is a regular bracket sequence, and the number of such substrings. If there are no such substrings, write the only line containing "0 1".

Examples

Input

)((())))(()())


Output

6 2


Input

))(


Output

0 1
"""

def find_longest_regular_bracket_sequence(bracket_string: str) -> tuple[int, int]:
    n = len(bracket_string)
    stack = []
    mapping = [0] * n
    
    # Build the mapping of opening brackets to their corresponding closing brackets
    for idx, char in enumerate(bracket_string):
        if char == '(':
            stack.append(idx)
        elif char == ')' and stack:
            mapping[stack.pop()] = idx
    
    # Find the longest regular bracket sequence and its count
    i = 0
    mx = 0
    cnt = 1
    tmp_max = 0
    prev_join_idx = 0
    
    while i < n:
        if mapping[i]:
            curr_len = mapping[i] - i + 1
            if i == prev_join_idx + 1:
                tmp_max += curr_len
            else:
                tmp_max = curr_len
            if tmp_max > mx:
                mx = tmp_max
                cnt = 1
            elif tmp_max == mx:
                cnt += 1
            prev_join_idx = mapping[i]
            i = mapping[i] + 1
        else:
            i += 1
    
    return mx, cnt