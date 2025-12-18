"""
QUESTION:
You are given an array A of size N. The array contains almost distinct elements with some duplicated. You have to print the elements in sorted order which appears more than once. 
Input Format:
The first line of input contains T, denoting the number of testcases. T testcases follow. Each testcase contains two lines of input.  The first line of input contains size of array N. The second line contains N integers separated by spaces.
Output Format:
For each test case, in a new line, print the required answer. If there are no duplicates print -1.
Your Task:
Your task is to complete the function SortedDuplicates(arr, n) which accepts array and its size as an argument. 
Constraints:
1 <= T <= 100
1 <= N <= 100
1 <= A_{i} <= 10^{6}
Examples:
Input:
1
9
3 4 5 7 8 1 2 1 3
Output:
1 3
"""

from typing import List
from collections import Counter

def find_sorted_duplicates(arr: List[int], n: int) -> List[int]:
    # Count the frequency of each element in the array
    frequency = Counter(arr)
    
    # Collect elements that appear more than once
    duplicates = [num for num in frequency if frequency[num] > 1]
    
    # Sort the duplicates
    duplicates.sort()
    
    # If no duplicates are found, return [-1]
    if not duplicates:
        return [-1]
    
    return duplicates