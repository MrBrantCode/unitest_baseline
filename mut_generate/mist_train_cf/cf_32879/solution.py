"""
QUESTION:
Write a function `process_input(strin: str) -> List[Tuple[str, str]]` that takes a string `strin` as input, where the string consists of multiple lines separated by `$$\n` and each line contains three elements separated by `\t`. The function should extract the second element from each line and a sequence from the third element of each line. The sequence should be cut into segments of length 60. The function should then return a list of tuples, where each tuple contains the extracted second element and the segmented sequence joined by newline characters.

The function should assume that the input string is well-formed and that each line has at least three elements separated by `\t`. The function should also assume that the third element of each line is a string that can be segmented into substrings of length 60.
"""

from typing import List, Tuple

def process_input(strin: str) -> List[Tuple[str, str]]:
    strin_split = strin.split('$$\n')[:-1]
    strin_split_content = [line.split('\n')[0] for line in strin_split]
    strout_seq = [line.split('\t')[2] for line in strin_split_content]
    strout_name = [line.split('\t')[1] for line in strin_split_content]
    
    result = [(name, '\n'.join([seq[i:i+60] for i in range(0, len(seq), 60)])) for name, seq in zip(strout_name, strout_seq)]
    return result