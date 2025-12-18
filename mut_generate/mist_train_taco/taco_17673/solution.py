"""
QUESTION:
CodeswarBala found various ornaments in Btyeland. Each ornament is made up of  various items, and each item is represented by a letter from 'a' to 'z'. An item can be present multiple times in a ornament . An item is called special item  if it occurs at least once in each of the ornament.

Given the list of N ornaments with their compositions, display the number of special items that exist in those ornaments.

Input Format

The first line consists of an integer, N, the number of ornaments. 
Each of the next NNlines contains a ornaments'composition. Each composition consists of lower-case letters  as mentioned above.

Constraints 
1≤N≤100
1≤ length of each composition ≤100

Output Format

Print the number of special items that are common in these ornaments. If there are none, print 0.

SAMPLE INPUT
3
abcdde
baccd
eeabg

SAMPLE OUTPUT
2

Explanation

Only "a" and "b" are the two kinds of special elements, since these are the only characters that occur in every ornaments's composition.
"""

def count_special_items(ornaments):
    if not ornaments:
        return 0
    
    # Initialize a list to count occurrences of each item
    item_count = [0] * 26
    
    # Number of ornaments
    num_ornaments = len(ornaments)
    
    # Iterate over each ornament
    for ornament in ornaments:
        # Use a set to track unique items in the current ornament
        unique_items = set(ornament)
        
        # Increment the count for each unique item in the current ornament
        for item in unique_items:
            item_count[ord(item) - ord('a')] += 1
    
    # Count the number of special items
    special_item_count = sum(1 for count in item_count if count == num_ornaments)
    
    return special_item_count