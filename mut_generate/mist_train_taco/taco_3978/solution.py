"""
QUESTION:
Consider a string A = "12345".  An infinite string is built by performing infinite steps on A recursively. In i^{th} step, A is concatenated with ‘$’ i times followed by reverse of A, that is, A = A | $...$ | reverse(A), where | denotes concatenation.
Given a position pos, find out the character at pos in the infinite string.
Example 1:
Input: pos = 3
Output: 3
Explanation: A = "12345", then A[pos] is 3.
Example 2:
Input: pos = 10
Output: 2
Explanation: A = "12345$54321", then A[pos] is 2.
Your Task:  
You dont need to read input or print anything. Complete the function posInfinite() which takes pos as input parameter and returns the character in the infinite string at pos.
Expected Time Complexity: O(sqrtn)
Expected Auxiliary Space: O(1)
Constraints:
1<= pos <=10^{12}
"""

def find_character_at_position(pos):
    A = '12345'

    def find_iteration(pos):
        n = 10 ** 3
        length = 5
        iteration = 0
        for i in range(1, n):
            length = 2 * length + i
            if length > pos:
                iteration = i
                break
        return (iteration, length)

    def recursive_search(length, iteration, pos):
        if pos <= 5:
            return A[pos - 1]
        part_length = (length - iteration) // 2
        (left, mid, right) = (part_length, iteration, part_length)
        if pos <= left:
            pass
        elif pos <= left + mid:
            return '$'
        else:
            pos = pos - (left + mid)
            pos = left - pos + 1
        return recursive_search(left, iteration - 1, pos)

    (iteration, length) = find_iteration(pos)
    return recursive_search(length, iteration, pos)