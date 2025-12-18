"""
QUESTION:
-----
ARRAY AND DISTINCT ELEMENTS
-----

Chef is multitalented but he mistakenly took part in 2 contest which will take place
at the same time. So while chef is busy at one cooking contest, he wants you to
take part in coding contest. Chef wants u to solve this program for him.

	

You have been given an array of size n. You have to calculate a subarray of size k
with maximum sum having distinct elements same as original array.

		
		

-----Input Format-----

First line contains no. of test cases. Second line contains n and k. Third line
contains array of n integers.


-----Output-----

Print maximum possible sum as stated in question

		
		

-----Example Text Case-----
Input:

1
10 6
8 8 3 5 3 8 5 7 7 7

Output:
37
"""

def max_sum_distinct_subarray(n, k, arr):
    # Convert the array to a set to get the number of distinct elements
    distinct_elements = set(arr)
    num_distinct = len(distinct_elements)
    
    max_sum = -1
    
    # Iterate over all possible subarrays of size k
    for i in range(n - k + 1):
        subarray = arr[i:i + k]
        subarray_set = set(subarray)
        
        # Check if the subarray has the same number of distinct elements as the original array
        if len(subarray_set) == num_distinct:
            subarray_sum = sum(subarray)
            if subarray_sum > max_sum:
                max_sum = subarray_sum
    
    return max_sum