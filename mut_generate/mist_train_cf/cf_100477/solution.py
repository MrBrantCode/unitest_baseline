"""
QUESTION:
Create a function named `sort_median_strength` that takes a list of lists `x` as input where each sublist represents a character's strength attributes. The function should return a list of median strengths for each character, sorted in ascending order. Each sublist may have an even or odd number of elements, and if it has an even number of elements, the median should be the average of the two middle elements. The function should handle the sorting of the median strengths based on the characters' attributes.
"""

def sort_median_strength(x):
    # create a list to store median strengths
    median_strengths = []
    
    # loop through each sublist in x
    for character in x:
        # sort the sublist in ascending order
        character.sort()
        
        # find the median strength of the character
        n = len(character)
        if n % 2 == 0:
            median = (character[n//2-1] + character[n//2]) / 2
        else:
            median = character[n//2]
        
        # append the median strength to the median_strengths list
        median_strengths.append(median)
    
    # sort the median_strengths list in ascending order
    median_strengths.sort()
    
    # return the sorted median_strengths list
    return median_strengths