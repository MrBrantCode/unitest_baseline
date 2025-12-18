"""
QUESTION:
Given a positive integer N, the task is to find all the N bit binary numbers having more than or equal 1’s than 0’s for any prefix of the number. 
Example 1:
Input:  N = 2
Output: 11 10
Explanation: 11 and 10 have more than 
or equal 1's than 0's
Example 2:
Input:  N = 3
Output: 111 110 101
Explanation: 111, 110 and 101 have more 
than or equal 1's than 0's
User Task:
Your task is to complete the function NBitBinary() which takes a single number as input and returns the list of strings in decreasing order. You need not take any input or print anything.
Expected Time Complexity: O(|2^{N}|)
Expected Auxiliary Space: O(2^{N})
Constraints:
1 <= N <= 20
"""

def generate_n_bit_binary_numbers(N):
    def solve(one, zero, op, N, answer):
        if N == 0:
            answer.append(op)
            return
        elif one > zero:
            op1 = op + '1'
            op2 = op + '0'
            solve(one + 1, zero, op1, N - 1, answer)
            solve(one, zero + 1, op2, N - 1, answer)
        elif one == zero:
            op = op + '1'
            solve(one + 1, zero, op, N - 1, answer)

    one = 1
    zero = 0
    op = '1'
    answer = []
    solve(one, zero, op, N - 1, answer)
    return answer