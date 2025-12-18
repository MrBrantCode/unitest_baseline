"""
QUESTION:
Write a function called `swap_pairs` that takes an alphanumeric sequence and the number of swaps as input. The function should swap the first 'n' pairs of characters in the sequence, where 'n' is the number of swaps. Each swap should exchange the characters at the even index with the character at the next odd index. The function should return the modified sequence as a string.
"""

def swap_pairs(sequence, swaps):
    """
    This function swaps the first 'n' pairs of characters in a given alphanumeric sequence.
    
    Parameters:
    sequence (str): The input alphanumeric sequence.
    swaps (int): The number of swaps to be performed.
    
    Returns:
    str: The modified sequence after swapping 'n' pairs of characters.
    """
    sequence = list(sequence)  
    for i in range(min(swaps, len(sequence)//2)):  
        sequence[i*2], sequence[i*2+1] = sequence[i*2+1], sequence[i*2]  
    return ''.join(sequence) 