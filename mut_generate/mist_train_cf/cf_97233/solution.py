"""
QUESTION:
Write a function called `print_star_grid` that takes an even integer n as input and prints an n x n grid with stars. Each row of the grid should contain n/2 stars, arranged in a pattern such that the number of consecutive stars increases by 1 from left to right and then decreases by 1 from right to left. The function should have a time complexity of O(n^2) and a space complexity of O(n).
"""

def print_star_grid(n):
    if n % 2 != 0:
        print("Error: n should be an even number.")
        return
    
    num_stars = n // 2
    
    for i in range(n):
        num_consecutive_stars = min(i+1, n-i, num_stars)
        
        for j in range(num_consecutive_stars):
            print("*", end=" ")
        
        print()