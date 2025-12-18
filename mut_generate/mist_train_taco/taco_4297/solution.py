"""
QUESTION:
Given an array p[] of length n used to denote the dimensions of a series of matrices such that dimension of i'th matrix is p[i] * p[i+1]. There are a total of n-1 matrices. Find the most efficient way to multiply these matrices together. 
The problem is not actually to perform the multiplications, but merely to decide in which order to perform the multiplications such that you need to perform minimum number of multiplications. There are many options to multiply a chain of matrices because matrix multiplication is associative i.e. no matter how one parenthesize the product, the result will be the same.
Example 1:
Input: 
n = 5
p[] = {1, 2, 3, 4, 5}
Output: (((AB)C)D)
Explaination: The total number of 
multiplications are (1*2*3) + (1*3*4) 
+ (1*4*5) = 6 + 12 + 20 = 38.
 
Example 2:
Input: 
n = 3
p = {3, 3, 3}
Output: (AB)
Explaination: The total number of 
multiplications are (3*3*3) = 27.
 
Your Task:
You do not need to read input or print anything. Your task is to complete the function matrixChainOrder() which takes n and p[] as input parameters and returns the string with the proper order of parenthesis for n-1 matrices. Use uppercase alphabets to denote each matrix.
Expected Time Complexity: O(n^{3})
Expected Auxiliary Space: O(n^{2})
Constraints:
2 ≤ n ≤ 26 
1 ≤ p[i] ≤ 500
"""

def matrix_chain_order(p, n):
    def show_brackets(i, j, brackets):
        nonlocal char, cnt, string
        if i == j:
            if cnt != 0:
                string += chr(ord(char) + cnt)
            else:
                string += char
            if char == 'Z':
                char = 'A'
                cnt += 1
            else:
                char = chr(ord(char) + 1)
        else:
            string += '('
            show_brackets(i, brackets[i][j], brackets)
            show_brackets(brackets[i][j] + 1, j, brackets)
            string += ')'
        return string

    n -= 1
    ans = [[0] * n for _ in range(n)]
    brackets = [[0] * n for _ in range(n)]
    size, j = 1, 0
    cost = 0
    char = 'A'
    cnt = 0
    string = ''

    while size < n:
        i = 0
        while i < n - size:
            j = i + size
            ans[i][j] = sys.maxsize
            k = i
            while k < j:
                cost = ans[i][k] + ans[k + 1][j] + p[i] * p[j + 1] * p[k + 1]
                if cost < ans[i][j]:
                    ans[i][j] = cost
                    brackets[i][j] = k
                k += 1
            i += 1
        size += 1

    return show_brackets(0, n - 1, brackets)