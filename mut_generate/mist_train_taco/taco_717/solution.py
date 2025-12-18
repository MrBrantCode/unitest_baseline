"""
QUESTION:
As you know Appu created aversion to Maths after that maths problem given by his teacher.So he stopped studying and began to do farming. He has some land where he starts growing sugarcane. At the end of the season he grew N sugarcanes. Is Appu satisfied??. No,
He wants all his sugar canes to be of the same height. He goes to the nearby market .He finds a powder which when applied to one of his sugarcanes will double the height of that sugar cane. Now he needs to find out whether is it possible to make all the sugarcanes of the same height . Oh No!! Again maths.
Please help him to find whether is it possible make all the sugar cane of the same height?

Input 
        First line contains N - the number of sugarcanes.Next N lines contains heights of sugarcanes seperated by space

Output
        Print "YES" if  it is possible make all the sugar cane of the same height or 
    "NO" otherwise (quotes only for clarity)

Constraints
        1 ≤ N ≤ 50 
         Initial Height of  all sugarcanes will be between 1 and 1,000,000,000, inclusive.

SAMPLE INPUT
2
1 23

SAMPLE OUTPUT
NO
"""

def can_make_sugarcanes_same_height(N, heights):
    if N < 1 or N > 50:
        raise ValueError("Number of sugarcanes must be between 1 and 50 inclusive.")
    
    for height in heights:
        if height < 1 or height > 1000000000:
            raise ValueError("Height of sugarcanes must be between 1 and 1,000,000,000 inclusive.")
    
    # Normalize all heights by repeatedly dividing by 2
    normalized_heights = []
    for height in heights:
        while height % 2 == 0:
            height //= 2
        normalized_heights.append(height)
    
    # Check if all normalized heights are the same
    if all(h == normalized_heights[0] for h in normalized_heights):
        return "YES"
    else:
        return "NO"