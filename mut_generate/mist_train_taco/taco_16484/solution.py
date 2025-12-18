"""
QUESTION:
Read problems statements in Mandarin Chinese and Russian as well. 

Today is Devu's birthday. He has obtained few colored balloons from his friends. You are given this information by a string s consisting of lower case English Latin letters. Each letter (from 'a' to 'z')  denotes a color. e.g. if s = "aab", then it means that he has received two balloons of color 'a' whereas one balloon of color 'b'.

Now, Devu wants to decorate the cake by arranging all the balloons linearly from left to right on the cake such that no same colored balloons are nearby/ adjacent to each other.

Now Devu wonders whether it is possible to do so or not? Please help him in this. If it is not possible to do so, print -1. Otherwise, print any one of arrangements of the balloons on the cake. If there are more than one possible ways of doing so, you can print any one of them. 

------ Input ------ 

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
First line of each test case will contain string s

------ Output ------ 

Print a single line corresponding to the answer of the problem.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ size of string s  ≤ 10^{5}$
$Sum of size of string s over all test cases will be less than or equal to ≤ 10^{6}$

----- Sample Input 1 ------ 
3
aab
ab
aa
----- Sample Output 1 ------ 
aba
ab
-1
----- explanation 1 ------ 
Example case 1. He can arrange the balloons in the order given by the following string "aba". 
Example case 2. He can arrange the balloons in the order given by the following string "ab"
Example case 3. There is no valid way of decorating cakes with balloon in the desired way. So we print -1.
"""

def arrange_balloons(s: str) -> str:
    from collections import Counter
    
    # Count the frequency of each character
    count = Counter(s)
    
    # Find the character with the maximum frequency
    max_char, max_count = max(count.items(), key=lambda item: item[1])
    
    # If the maximum frequency is greater than half the length of the string plus one,
    # it's impossible to arrange the balloons without having two same colored balloons adjacent
    if max_count > (len(s) + 1) // 2:
        return "-1"
    
    # Create a list to store the result
    result = []
    
    # Create a list of tuples (character, count) sorted by count in descending order
    sorted_chars = sorted(count.items(), key=lambda item: item[1], reverse=True)
    
    # Alternate placing the characters to avoid adjacent same characters
    while sorted_chars:
        if result and result[-1] == sorted_chars[0][0]:
            # If the last character in result is the same as the most frequent character,
            # place the second most frequent character first
            result.append(sorted_chars[1][0])
            sorted_chars[1] = (sorted_chars[1][0], sorted_chars[1][1] - 1)
            if sorted_chars[1][1] == 0:
                sorted_chars.pop(1)
        else:
            # Place the most frequent character
            result.append(sorted_chars[0][0])
            sorted_chars[0] = (sorted_chars[0][0], sorted_chars[0][1] - 1)
            if sorted_chars[0][1] == 0:
                sorted_chars.pop(0)
        
        # Sort the list again to maintain the order by frequency
        sorted_chars.sort(key=lambda item: item[1], reverse=True)
    
    return ''.join(result)