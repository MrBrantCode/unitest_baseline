"""
QUESTION:
Create a function `find_highest_peak` that takes an array of elevation data as input and returns the index of the highest peak. The highest peak must be surrounded by at least two valleys, which are defined as adjacent elements that are both lower than the peak.

The input array will have a length not exceeding 10^5, and the values in the array will be integers ranging from 0 to 10^9. The time complexity of the solution should not exceed O(nlogn) and the space complexity should not exceed O(n). Assume that there will always be at least one peak satisfying the condition.
"""

def find_highest_peak(arr):
    n = len(arr)
    
    # Create two arrays to store the indices of the valleys and peaks
    valleys = []
    peaks = []
    
    # Iterate through the array to find the valleys and peaks
    for i in range(1, n-1):
        if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
            valleys.append(i)
        elif arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            peaks.append(i)
    
    # Iterate through the peaks to find the highest peak surrounded by two valleys
    highest_peak = -1
    highest_peak_value = float('-inf')
    for peak in peaks:
        left_valley = -1
        right_valley = n
        for valley in valleys:
            if valley < peak:
                left_valley = valley
            else:
                right_valley = valley
                break
        if left_valley != -1 and right_valley != n and arr[peak] > highest_peak_value:
            highest_peak = peak
            highest_peak_value = arr[peak]
    
    return highest_peak