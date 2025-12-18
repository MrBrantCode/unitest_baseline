"""
QUESTION:
Write a function `find_k_most_common` that takes as input an array of integers and an integer `k`, and returns a list of tuples, each containing a value and its frequency, sorted in descending order of frequency. In case of ties, return the values with the lowest indices in the array first. The array will contain at least 100 elements and at most 10000 elements, with integers between -10000 and 10000. The time complexity should be O(nlogk), where n is the size of the array and k is the number of most common values to find.
"""

import heapq

def find_k_most_common(array, k):
    frequency = {}
    
    # Calculate the frequency of each value
    for value in array:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1
    
    # Create a heap of k most common values
    heap = []
    for value, freq in frequency.items():
        heapq.heappush(heap, (freq, value))
        if len(heap) > k:
            heapq.heappop(heap)
    
    # Convert heap to a list of tuples
    k_most_common = []
    while heap:
        freq, value = heapq.heappop(heap)
        k_most_common.append((value, freq))
    
    # Reverse the list to sort it in descending order of frequency
    k_most_common.reverse()
    
    return k_most_common