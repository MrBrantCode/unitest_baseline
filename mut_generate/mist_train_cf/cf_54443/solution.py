"""
QUESTION:
You need to implement a function `minHeightShelves(books, shelf_width, shelf_weight, shelf_height)` that takes four parameters: a 2D list `books` where each sublist contains three integers representing the thickness, height, and weight of a book, and three integers `shelf_width`, `shelf_weight`, and `shelf_height` representing the maximum width, weight, and height of a shelf, respectively.

The function should return the minimum possible height that the total bookshelf can be after placing shelves in this manner, while also ensuring that no shelf exceeds the weight and height limit. The order of the books must remain the same as in the input list.

Constraints: 
`1 <= len(books) < 1000`
`1 <= books[i][0] <= shelf_width <= 1000`
`1 <= books[i][1] <= shelf_height <= 1000`
`1 <= books[i][2] <= shelf_weight <= 1000`
"""

def minHeightShelves(books, shelf_width, shelf_weight, shelf_height):
    n = len(books)
    dp = [0] + [10000]*n
    for i in range(1, n+1):
        max_height = 0
        total_width = 0
        total_weight = 0
        j = i
        while j > 0:
            total_width += books[j-1][0]
            total_weight += books[j-1][2]
            max_height = max(max_height, books[j-1][1])
            if total_width > shelf_width or total_weight > shelf_weight or max_height > shelf_height:
                break
            dp[i] = min(dp[i], dp[j-1] + max_height)
            j -= 1
    return dp[-1]