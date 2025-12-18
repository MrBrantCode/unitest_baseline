"""
QUESTION:
Ma5termind and Subway are bored of their normal life.They want to do something interesting so that they can enjoy their last sem of college life.As usual Ma5termind comes up with a simple and interesting game.

Ma5termind gives Subway a compressed string. A compressed String is composed of characters and numbers.Every character in a compressed string contains a number. Ex a3b1c2 it represents aaabcc. Other compressed string could be a22b2a1 , z5c2x36. Each number in the compressed string indicates the number of times the corresponding character occurs in the string. The final string is 1 indexed.  Ma5termind wants Subway to sort the compressed string and tell him the kth character in the sorted compressed string.Since subway got speed Ma5termind asks him various such questions.

Help Subway in answering Ma5termind's question.

Input:

The first line contains the compressed string.This is followed by Q that indicates the number of questions Ma5termind shoots on Subway.Follows Q lines each line contain an integer K.

Output:

For every question output the Kth  character if it exists else print -1 .

Constraints:

2 ≤ Length of Compressed String ≤ 10^4

1 ≤ Length of Final String ≤ 10^18

1 ≤ Q ≤ 10^5

1 ≤ K ≤ 10^18

Every character in the string is lowercase English letter.

Note:

The number for a character may contain leading zeroes.

SAMPLE INPUT
a2b3c2a1
4
2
5
1
8

SAMPLE OUTPUT
a
b
a
c

Explanation

The final sorted string is aaabbbcc.
"""

import re

def find_kth_character(compressed_string, queries):
    # Step 1: Parse the compressed string
    match = re.findall("([a-z])(\d+)", compressed_string)
    
    # Step 2: Create a frequency dictionary
    freq_char = {}
    for each_tuple in match:
        freq_char[each_tuple[0]] = 0
    
    for each_tuple in match:
        freq_char[each_tuple[0]] += int(each_tuple[1])
    
    # Step 3: Sort the characters
    chars = sorted(freq_char.keys())
    
    # Step 4: Calculate cumulative frequencies
    prev = 0
    for char in chars:
        freq_char[char] += prev
        prev = freq_char[char]
    
    # Step 5: Function to find the Kth character
    def find_char(chars, freq_dict, index):
        prev = 0
        for char in chars:
            if index >= prev and index <= freq_dict[char]:
                return char
            prev = freq_dict[char]
        return -1
    
    # Step 6: Process each query
    results = []
    for index in queries:
        results.append(find_char(chars, freq_char, index))
    
    return results