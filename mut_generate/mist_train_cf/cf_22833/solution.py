"""
QUESTION:
Create a function `find_highest_peak(arr)` that takes an array of integers as input and returns the index of the highest peak, where a peak is defined as an element that is greater than its adjacent elements and has at least two valleys on either side, with a valley being an element that is lower than its adjacent element. The function should have a time complexity of O(nlogn) and a space complexity of O(n). If no such peak exists, return -1.
"""

def find_highest_peak(arr):
    n = len(arr)
    peaks = []
    
    # Finding all the peaks in the array
    for i in range(1, n-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            peaks.append(i)
    
    # Checking if the peaks have at least two valleys on either side
    for peak in peaks:
        left_valleys = 0
        right_valleys = 0
        
        # Counting the number of valleys on the left side of the peak
        for i in range(peak-1, 0, -1):
            if arr[i] < arr[i-1]:
                left_valleys += 1
            else:
                break
        
        # Counting the number of valleys on the right side of the peak
        for i in range(peak+1, n-1):
            if arr[i] < arr[i+1]:
                right_valleys += 1
            else:
                break
        
        # Checking if the peak has at least two valleys on both sides
        if left_valleys >= 2 and right_valleys >= 2:
            return peak
    
    return -1