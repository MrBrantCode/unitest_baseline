"""
QUESTION:
Bob is very fond of balloons. Once he visited an amusement park with his mother. The mother told Bob that she would buy him a balloon only if he answer her problem right. She gave Bob a string S [contains only lowercase characters] and asked him to use the characters of string to form as many instances of the word "balloon" as possible. Return the maximum number of instances that can be formed.
Help Bob to solve the problem.
Note: You can use each character in the string at most once. 
Example 1:
Input:
S: nlaebolko
Output: 1
Explanation:
Here, the number of occurence of 'b' = 1
of occurence of 'a' = 1
of occurence of 'l' = 2
of occurence of 'o' = 2
of occurence of 'n' = 1
So, we can form 1 "balloon" using the letters.
 
Example 2: 
Input:
S: loonbalxballpoon
Output: 2
Explanation:
Here, the number of occurence of 'b' = 2
of occurence of 'a' = 2
of occurence of 'l' = 4
of occurence of 'o' = 4
of occurence of 'n' = 2
So, we can form 2 "balloon" using the letters.
 
Your Task:
The task is to complete the function maxInstance() which takes a string as the only input parameter and should return the maximum instances that can be formed of the word "balloon" using the given string.
Expected Time Complexity: O(n), n is size of the given string.
Expected Auxiliary Space: O(26).
Constraints:
1 <= s.length <= 10^{6}
"""

from collections import Counter

def max_balloon_instances(s: str) -> int:
    # Count the frequency of each character in the string
    char_count = Counter(s)
    
    # Define the required characters and their counts for one "balloon"
    required_chars = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
    
    # Initialize the maximum instances to a large number
    max_instances = float('inf')
    
    # Calculate the maximum instances of "balloon" that can be formed
    for char, count in required_chars.items():
        if char in char_count:
            max_instances = min(max_instances, char_count[char] // count)
        else:
            # If any required character is missing, we can't form any "balloon"
            return 0
    
    return max_instances