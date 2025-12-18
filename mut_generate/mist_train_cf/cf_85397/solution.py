"""
QUESTION:
Create a function named `rolling_avg_median_and_frequency` that takes a list of unique real numbers as input. The function should return a tuple containing a list of tuples, where each tuple contains the dynamic average and median of the numbers processed so far, and a dictionary where the keys are the numbers and the values are their frequencies. The list of tuples should not contain any duplicates. The function should update the dictionary and calculate the average and median after processing each number in the list. The input list can contain decimal, negative numbers, or zeroes.
"""

from typing import List, Tuple, Dict, Union
import numpy as np

def rolling_avg_median_and_frequency(numbers: List[Union[float,int]]) -> Tuple[List[Tuple[float, float]], Dict[float, int]]:
    """
    Function to get the rolling average, median and frequency of numbers in a list
    """
    stats = []
    freq_dict = {}
    for i, num in enumerate(numbers):
        # Update frequency dictionary
        freq_dict[num] = freq_dict.get(num, 0) + 1 
        
        # Calculate rolling average and median
        avg = np.mean(numbers[0:i+1])
        median = np.median(numbers[0:i+1])
        
        stats.append((avg, median))
    
    return stats, freq_dict