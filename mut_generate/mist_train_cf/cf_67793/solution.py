"""
QUESTION:
Write a function `minHeightShelves(books, shelf_width, shelf_weight)` that takes a list of books where each book is a list of three integers representing the book's thickness, height, and weight, as well as the shelf's width and weight capacity. Return the minimum possible height of the bookshelf that can be achieved by placing the books onto shelves without exceeding the shelf's width and weight capacity. The function should work for up to 1000 books, with each book's thickness, height, and weight, as well as the shelf's width and weight capacity, ranging from 1 to 1000.
"""

def minHeightShelves(books, shelf_width, shelf_weight):
    n = len(books)
    dp = [0] + [float('inf')] * n  
    for i in range(1, n + 1):
        widest = weights = heights = 0
        j = i
        while j > 0:
            widest += books[j - 1][0]
            weights += books[j - 1][2]
            heights = max(heights, books[j - 1][1])
            if widest > shelf_width or weights > shelf_weight:
                break
            dp[i] = min(dp[i], heights + dp[j - 1])
            j -= 1
    return dp[-1]