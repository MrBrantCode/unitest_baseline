"""
QUESTION:
No description!!!

Input  :: [10,20,25,0]

Output :: ["+0", "+10", "+15", "-10"] 

`Show some love, rank and upvote!`
"""

def equalize_array(arr):
    return ['{:+d}'.format(i - arr[0]) for i in arr]