"""
QUESTION:
Write a function named `MostCommon` that takes an array of integers as input and returns a dictionary containing the most frequent numbers in the array along with their counts. If there are multiple numbers with the same highest frequency, include all of them in the dictionary. If the input array is empty, return an empty dictionary.
"""

def MostCommon(arr):
    if not arr: 
        return {}
    
    freq_dict = {i: arr.count(i) for i in arr} 
    max_freq = max(freq_dict.values())
  
    return {i: freq for i, freq in freq_dict.items() if freq == max_freq}