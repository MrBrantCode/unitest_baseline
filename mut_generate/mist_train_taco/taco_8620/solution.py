"""
QUESTION:
you are given an array of size N. You need to select K elements from the array such that the difference between the max number among selected and the min number among selected array elements should be minimum. Print the minimum difference.

INPUT:
First line N number i.e., length of array
Second line K number 
Next N lines contains a number for each line

OUTPUT:
Print the minimum possible difference

0<N<10^5
0<K<N
0<number<10^9

SAMPLE INPUT
5
3
1
2
3
4
5

SAMPLE OUTPUT
2
"""

def find_min_difference(arr, K):
    # Sort the array
    arr.sort()
    
    # Calculate the minimum difference
    min_diff = min(arr[i + K - 1] - arr[i] for i in range(len(arr) - K + 1))
    
    return min_diff