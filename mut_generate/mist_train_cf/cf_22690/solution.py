"""
QUESTION:
Write a function named `calculate_intersection_set_properties` that takes two sets of integers as input. The function should return a tuple containing the sum of the intersection set and the count of elements in the intersection set that are divisible by 3 and less than 10. The intersection set should not contain duplicates and should be sorted in descending order.
"""

def calculate_intersection_set_properties(setA, setB):
    """
    This function calculates the sum of the intersection set and the count of elements 
    in the intersection set that are divisible by 3 and less than 10.

    Args:
        setA (set): The first set of integers.
        setB (set): The second set of integers.

    Returns:
        tuple: A tuple containing the sum of the intersection set and the count of elements 
        in the intersection set that are divisible by 3 and less than 10.
    """

    # Intersection of setA and setB
    intersection = setA.intersection(setB)

    # Sort elements in descending order
    intersection = sorted(intersection, reverse=True)

    # Sum of all elements in the intersection set
    sum_of_elements = sum(intersection)

    # Number of elements divisible by 3 and less than 10
    divisible_by_3_and_less_than_10 = len([x for x in intersection if x % 3 == 0 and x < 10])

    return sum_of_elements, divisible_by_3_and_less_than_10