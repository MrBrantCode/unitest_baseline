"""
QUESTION:
Let Max be the maximum possible mean of a multiset of values obtained from an array Arr of length N. Let Min be the minimum possible mean of a multiset of values obtained from the same array. Note that in a multiset values may repeat. The task is to find the number of multisets with mean as Max and the number of multisets with mean as Min. The answer may be too large so output the number of multisets modulo 10^{9}+7. 
 
Example 1:
Input:
N = 5
Arr = {3, 1, 2, 3, 4} 
Output:
1 1
Explanation:
The maximum possible Mean of a Subset
of the array is 4. There can be only 1
such subset - {3, 1, 2, 3, 4}.
The minimum possible Mean of a Subset
of the array is 1. There can be only 1
such subset - {3, 1, 2, 3, 4}.
Example 2:
Input:
N = 3
Arr = {1, 2, 1} 
Output:
1 3
Explanation:
The maximum possible Mean of a Subset
of the array is 2. There can be only 1
such subset - {1, 2, 1}.
The minimum possible Mean of a Subset
of the array is 1. There can be 3 such
subsets - {1, 2, 1}; {1, 2, 1}; {1, 2, 1}.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function numOfSubsets() which takes an Integer N and an array Arr[] as input and returns a vector of two numbers- the number of multisets with mean as Max and the number of multisets with mean as Min.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
1 <= N <= 10^{5}
1 <= Arr[i] <= 10^{5}
"""

def num_of_subsets(N, Arr):
    mod = 1000000007
    
    # Find the minimum and maximum values in the array
    mn = min(Arr)
    mx = max(Arr)
    
    # Count the occurrences of the minimum and maximum values
    mnc = Arr.count(mn)
    mxc = Arr.count(mx)
    
    # Calculate the number of subsets with mean as max and min
    r1 = pow(2, mnc, mod) - 1
    r2 = pow(2, mxc, mod) - 1
    
    return (r2, r1)