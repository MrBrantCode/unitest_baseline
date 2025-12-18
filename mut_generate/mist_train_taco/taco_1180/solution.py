"""
QUESTION:
Little Ashish got a lot of strings as his birthday gift. He does not mind getting so many strings for free; in fact, he loves them. But, on noticing all the strings he received as a gift, Little Ashish, who's also a snob and a bit OCD kind of a guy, realizes that he does not like the way in which the strings are arranged.

He likes his strings sorted, in a different kind of a way. He wants his strings to be sorted based on the count of characters present in the string. For instance, if the string is: "aaabbc", then the desired string would be: cbbaaa. In case where the count of two characters is same, then the lexicographically smaller one will be printed first. For instance: "aabbcc" then, the output will be: "aabbcc".

Input:
First line of input contains number of test cases T.   Each test case contains a single string S.  

Output:
For each test cases print the sorted string.  

Constraints:
1 ≤ T ≤ 100
1 ≤ |S| ≤ 100  

Note:
String contains only lowercase characters ['a' to 'z']. 

SAMPLE INPUT
3
aabbccdd
aabcc
hackerearthSAMPLE OUTPUT
aabbccdd
baacc
cktaaeehhrr
"""

def sort_string_by_char_count(s: str) -> str:
    # Create a dictionary to count the frequency of each character
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Create a list of tuples (count, character) and sort it
    sorted_char_count = sorted([(count, char) for char, count in char_count.items()], reverse=True)
    
    # Build the sorted string based on the sorted list
    sorted_string = ""
    for count, char in sorted_char_count:
        sorted_string += char * count
    
    return sorted_string