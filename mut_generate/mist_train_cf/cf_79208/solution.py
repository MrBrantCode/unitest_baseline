"""
QUESTION:
Write a function `jaccard_similarity(text1, text2)` that calculates the Jaccard Similarity Index between two input texts, considering the order of words and unique words in the texts. The function should return the similarity as a percentage rounded off to two decimal places. Ensure the implementation handles potential edge cases such as empty strings or non-string inputs. The function should return `None` for non-string inputs and 0.0 for empty strings.
"""

def jaccard_similarity(text1, text2):
    # Checking input type for potential edge cases
    if not isinstance(text1, str) or not isinstance(text2, str):
        return None
        
    # Handling edge case of empty strings
    if len(text1) == 0 or len(text2) == 0:
        return 0.0
       
    # Converting the strings to sets
    set1 = set(text1.split())
    set2 = set(text2.split())
    
    # Finding the intersection and union of the two sets
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    
    # Calculating the Jaccard Similarity index
    similarity = float(len(intersection))/len(union)
    
    # Converting to a percentage and rounding off to two decimal places
    similarity = round(similarity*100, 2)
    return similarity