"""
QUESTION:
In a party, there are 4 dress codes i.e. one can either wear Red(R) or Blue(B) or Green(G) or Yellow(Y). Photographer needs the most colorful picture possible, so he arranges people in a specific order like RGBYRGBY, RYBGRY, RYBGR, RGBYRGB but not in order like GGBRGBR, BGYBGY, GBGGBYR. Using the given information find out the number of people of a particular color required in the order (if there is a place for a particular color) to have the colorful picture. Given the order s you need to find out the required colour of every type. String lower than size 4 always contains the pattern. (Here '!' means empty.)
Example 1:
Input: s = YRGBYRGB
Output: R0G0B0Y0
Explaination: No colour is required as there 
is no empty space in the string.
Example 2:
Input: s = !!!!RYGB
Output: R1G1B1Y1
Explaination: To maintain the order the sequence 
will be 'RYGBRYGB'.
Your Task:
You do not need to read input or print anything. Your task is to complete the function extraCount() which takes string s and returns a list containing the number of required R, G, B and Y respectively.
Expected Time Complexity: O(|s|)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ |s| ≤ 1000
"""

def calculate_required_colors(s: str) -> list:
    # Initialize a list to count the required colors
    required_counts = [0, 0, 0, 0]
    
    # Iterate over the string in chunks of 4
    for i in range(0, len(s), 4):
        sub = s[i:i + 4]
        if 'R' not in sub:
            required_counts[0] += 1
        if 'G' not in sub:
            required_counts[1] += 1
        if 'B' not in sub:
            required_counts[2] += 1
        if 'Y' not in sub:
            required_counts[3] += 1
    
    return required_counts