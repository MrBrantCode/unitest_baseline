"""
QUESTION:
Construct a function called `construct_prime_matrix` that takes a list of numbers and an integer `n` as input, and returns a 2D list of size `n x n` such that the sum of each row and each column is equal to a prime number, and each element in the matrix is unique. The numbers in the input list should be used to fill the matrix without repetition.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def construct_prime_matrix(numbers, n):
    def backtrack(matrix, used, row, col):
        if row == n:
            return True
        
        for num in numbers:
            if num in used:
                continue
            
            matrix[row][col] = num
            
            if not is_prime(sum(matrix[row])):
                continue
            
            if not is_prime(sum(matrix[i][col] for i in range(n))):
                continue
            
            if matrix[row].count(num) > 1 or [matrix[i][col] for i in range(n)].count(num) > 1:
                continue
            
            used.append(num)
            
            if col == n-1:
                if backtrack(matrix, used, row+1, 0):
                    return True
            else:
                if backtrack(matrix, used, row, col+1):
                    return True
            
            used.remove(num)
        
        return False

    matrix = [[0] * n for _ in range(n)]
    used = []
    
    if backtrack(matrix, used, 0, 0):
        return matrix
    else:
        return "No valid solution found."