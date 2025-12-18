"""
QUESTION:
Given an array of integers, determine the minimum number of elements to delete to leave only elements of equal value.

Example  

$arr=[1,2,2,3]$  

Delete the $2$ elements $1$ and $3$ leaving $arr=[2,2]$. If both twos plus either the $1$ or the $3$ are deleted, it takes $3$ deletions to leave either $\left[3\right]$ or $\left[1\right]$.  The minimum number of deletions is $2$.

Function Description  

Complete the equalizeArray function in the editor below.  

equalizeArray has the following parameter(s):  

int arr[n]: an array of integers   

Returns  

int: the minimum number of deletions required  

Input Format

The first line contains an integer $n$, the number of elements in $\textbf{arr}$. 

The next line contains $n$ space-separated integers $arr\left[i\right]$.

Constraints

$1\leq n\leq100$
$1\leq arr[i]\leq100$

Sample Input
STDIN       Function
-----       --------
5           arr[] size n = 5
3 3 2 1 3   arr = [3, 3, 2, 1, 3]

Sample Output
2   

Explanation

Delete $arr[2]=2$ and $arr[3]=1$ to leave $ar r'=[3,3,3]$. This is minimal.  The only other options are to delete $4$ elements to get an array of either $\left[1\right]$ or $\left[2\right]$.
"""

def equalize_array(arr):
    # Dictionary to count the frequency of each element
    frequency = {}
    
    # Variable to keep track of the most frequent element
    most_frequent_element = arr[0]
    
    # Count the frequency of each element in the array
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
        
        # Update the most frequent element if necessary
        if frequency[num] > frequency[most_frequent_element]:
            most_frequent_element = num
    
    # Calculate the minimum number of deletions required
    min_deletions = len(arr) - frequency[most_frequent_element]
    
    return min_deletions