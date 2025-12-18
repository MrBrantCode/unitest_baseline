"""
QUESTION:
Write a function called `distributeBooks` that takes two parameters: `books` and `num_students`. `books` represents the total number of books to distribute, and `num_students` is the number of students in the row. The function should return an array of length `num_students` that represents the final distribution of books. The array should sum up to `books`. The distribution of books follows a pattern where the first student gets 1 book, the second student gets 2 books, and so on until the last student gets `num_students` books. After reaching the last student, the process repeats, incrementing the number of books given to each student by `num_students`. The process stops when all books have been distributed.

Constraints: 1 <= books <= 10^9, 1 <= num_students <= 1000.
"""

def distributeBooks(books, num_students):
    distribution = [0 for _ in range(num_students)]
    i = 0
    while books > 0:
        give = min(books, i+1)
        distribution[i%num_students] += give
        books -= give
        i += 1
    return distribution