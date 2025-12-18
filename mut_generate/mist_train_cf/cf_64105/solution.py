"""
QUESTION:
Develop a function `arrange_triplets(nums, ascending=True)` that takes a list of sequential integers and a boolean parameter `ascending` as input. The function should arrange the integers into triplets. If `ascending` is True, arrange the triplets in ascending order; otherwise, arrange them in descending order. If the length of the list is not a multiple of 3, handle the remaining integers by including them in the last triplet.
"""

def arrange_triplets(nums, ascending=True):
    """
    Arrange a list of sequential integers into triplets and sort them in ascending or descending order.
    
    Args:
    nums (list): A list of sequential integers.
    ascending (bool): A boolean parameter indicating whether to arrange the triplets in ascending or descending order. Defaults to True.
    
    Returns:
    list: A list of lists, where each sublist contains three or fewer integers in the specified order.
    """
    triples = [nums[n:n+3] for n in range(0, len(nums), 3)]
    return sorted(triples, key=lambda x: x[0], reverse=not ascending)