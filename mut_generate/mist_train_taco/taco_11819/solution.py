"""
QUESTION:
Given an array arr[] of size, N. Find the subarray with maximum XOR. A subarray is a contiguous part of the array.
Example 1:
Input:
N = 4
arr[] = {1,2,3,4}
Output: 7
Explanation: 
The subarray {3,4} has maximum xor 
value equal to 7.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function maxSubarrayXOR() which takes the array arr[], its size N as input parameters and returns the maximum xor of any subarray.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
1 <= N <= 10^{5}
1^{ }<= arr[i] <= 10^{5}
"""

def max_subarray_xor(arr, N):
    class TrieNode:
        def __init__(self):
            self.bits = {}
            self.val = None

    class Trie:
        def __init__(self) -> None:
            self.root = TrieNode()

        def insert(self, n):
            curr_node = self.root
            for i in range(31, -1, -1):
                bitVal = n >> i & 1
                if bitVal not in curr_node.bits:
                    curr_node.bits[bitVal] = TrieNode()
                curr_node = curr_node.bits[bitVal]
            curr_node.val = n

        def _find_Max_XOR(self, n):
            curr_node = self.root
            for i in range(31, -1, -1):
                bitVal = n >> i & 1
                if 1 - bitVal in curr_node.bits:
                    curr_node = curr_node.bits[1 - bitVal]
                elif bitVal in curr_node.bits:
                    curr_node = curr_node.bits[bitVal]
                else:
                    return 0
            return n ^ curr_node.val

        def maxXorSubarray(self, arr):
            max_xor = arr[0]
            prefix_xor = arr[0]
            self.insert(prefix_xor)
            for n in arr[1:]:
                prefix_xor = prefix_xor ^ n
                max_xor = max(max_xor, prefix_xor, self._find_Max_XOR(prefix_xor))
                self.insert(prefix_xor)
            return max_xor

    t = Trie()
    return t.maxXorSubarray(arr)