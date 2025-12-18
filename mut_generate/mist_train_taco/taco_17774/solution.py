"""
QUESTION:
The enmity between Logan and Donald Pierce  never ceases to exist.  
However, once Logan and Donald came face to face. Donald got agitated and asked Logan to prove his true mettle by solving a puzzle.   
Logan is provided an array Arr[] of  N  integers. He can select only a single integer from the array and can perform certain special operations on it any number of time.
An operation can be one of the following type : 
Decrement the integer by 1 provided that it is greater than 0
Increment the integer by 1

Donald asks Logan to tell the least number of operations required to obtain the smallest possible XOR sum of all the integers.
Since Logan is currently in hurry to meet Charles and Canibal, he asks you guys to solve this problem. Help him!! 
 
------ Input ------ 

First line contains an integer T denoting number of test cases. 
First line of each test case contains an integer N.
Second line of each test case contains N space separated integers
 
------ Output ------ 

For each test case, print an integer denoting the minimum number of required operations on a separate line.
 
------ Constraints ------ 

$1 ≤ T ≤ 10$
$1 ≤ N ≤ 10^{5}$
$0 ≤ Arr[i] ≤ 4294967296$
 
----- Sample Input 1 ------ 
1
4
1 1 1 1
----- Sample Output 1 ------ 
0
----- explanation 1 ------ 
Since the XOR sum of all numbers is 0 and can't be reduced further, the answer is 0.
"""

def min_operations_to_smallest_xor_sum(test_cases):
    results = []
    
    for case in test_cases:
        N, Arr = case
        xor = 0
        
        # Calculate the XOR sum of the array
        for num in Arr:
            xor ^= num
        
        # Find the minimum operations required
        min_operations = float('inf')
        for num in Arr:
            a = num
            b = a ^ xor
            min_operations = min(min_operations, abs(a - b))
        
        results.append(min_operations)
    
    return results