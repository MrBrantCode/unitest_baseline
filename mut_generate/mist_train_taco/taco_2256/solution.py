"""
QUESTION:
You're given a sequence of N distinct integers. You need to find a subsequence of length K with the maximum possible median.

The median of a sequence is the value of the element which is in the middle of the sequence after sorting it in non-decreasing order. If the length of the sequence is even, the left of two middle elements is selected. For example, if the sequence is [3, 4, 2, 1, 5], then the median is 3 since after sorting, it will look like [1, 2, 3, 4, 5] and 3 is the only middle element. The median of [4, 2, 1, 5] is 2 since after sorting, the value 2 is the left of the two middle elements 2 and 4.

A subsequence is a sequence that can be derived from the given sequence by deleting zero or more elements without changing the order of the remaining elements. For example, if the sequence is [2, 1, 4, 5, 7], then [1, 5, 7], [2, 1, 4], [5] are some valid subsequences but [4, 1, 2], [1, 6, 7] are not.

------ Input Format ------ 

- The first line will contain T, the number of test cases. The description of test cases follow.
- The first line of each test case consists of two space-separated integers N, the length of the sequence, and K, the length of the subsequence to be found.
- The second line of each test case consists of N distinct space-separated integers A_{i}, the elements of the sequence.

------ Output Format ------ 

- For each test case, output two lines.
- The first line should consist of the median of the subsequence with the maximum median.
- The second line should consist of K space-separated integers, representing a subsequence with that median. If there are multiple such subsequences, print any.

------ Constraints ------ 

$1 ≤ T ≤ 30$
$1 ≤ K ≤ N ≤ 2 \times 10^{5}$
$1 ≤ A_{i} ≤ 10^{9}$
- Sum of $N$ over all test cases won't exceed $5 \times 10^{5}$

----- Sample Input 1 ------ 
1
5 3
1 4 3 6 5
----- Sample Output 1 ------ 
5
1 6 5
"""

import math

def find_max_median_subsequence(sequence, subsequence_length):
    # Sort the sequence to find the median easily
    sorted_sequence = sorted(sequence)
    
    # Calculate the index of the median in the sorted subsequence
    median_index = (subsequence_length // 2)
    
    # The median is the element at the median_index position from the end in the sorted sequence
    median = sorted_sequence[-median_index - 1]
    
    # Initialize counters for elements less than, equal to, and greater than the median
    count = 0
    less_count = 0
    greater_count = 0
    
    # Initialize the result subsequence
    result_subsequence = []
    
    # Iterate through the original sequence to form the subsequence
    for num in sequence:
        if count == subsequence_length:
            break
        if num < median and less_count < math.ceil(subsequence_length / 2) - 1:
            result_subsequence.append(num)
            less_count += 1
            count += 1
        elif num == median:
            result_subsequence.append(num)
            count += 1
        elif num > median and greater_count < math.ceil((subsequence_length + 1) / 2):
            result_subsequence.append(num)
            greater_count += 1
            count += 1
    
    return median, result_subsequence