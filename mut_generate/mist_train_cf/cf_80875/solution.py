"""
QUESTION:
Write a function named `count_elephants` that takes an integer `total_animals` as input, representing the total number of animals in the zoo, which includes zebras, elephants, and other animals. The function should return the number of elephants. 

Note that the number of zebras is 60 more than three times the number of elephants, and the total number of animals does not exceed 350. The function should handle the case where the total number of animals is 0 or exceeds 350, and it should handle the case where the number of elephants is not an integer.
"""

def count_elephants(total_animals):
    if total_animals > 350:
        return "Total number of animals cannot exceed 350"
    for others in range(total_animals+1): 
        elephants = (total_animals - 60 - others) / 4
        if elephants < 0:
            continue  
        zebras = 3 * elephants + 60
        if others + zebras + elephants == total_animals:
            return elephants  