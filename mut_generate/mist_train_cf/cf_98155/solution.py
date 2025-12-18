"""
QUESTION:
Write a function named `sort_median_strength` that takes a 2D list `x` as input, where each sublist represents a character's strengths and contains unsorted integers between 1 and 10. The function should return a list of sorted median strengths, one for each character. If a sublist has an even number of elements, the median should be the average of the two middle elements.
"""

def sort_median_strength(x):
    median_strengths = []
    
    for character in x:
        character.sort()
        
        n = len(character)
        if n % 2 == 0:
            median = (character[n//2-1] + character[n//2]) / 2
        else:
            median = character[n//2]
        
        median_strengths.append(median)
    
    median_strengths.sort()
    
    return median_strengths