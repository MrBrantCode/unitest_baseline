"""
QUESTION:
Mr Keks is a typical white-collar in Byteland.

He has a bookshelf in his office with some books on it, each book has an integer positive price.

Mr Keks defines the value of a shelf as the sum of books prices on it. 

Miraculously, Mr Keks was promoted and now he is moving into a new office.

He learned that in the new office he will have not a single bookshelf, but exactly $k$ bookshelves. He decided that the beauty of the $k$ shelves is the bitwise AND of the values of all the shelves.

He also decided that he won't spend time on reordering the books, so he will place several first books on the first shelf, several next books on the next shelf and so on. Of course, he will place at least one book on each shelf. This way he will put all his books on $k$ shelves in such a way that the beauty of the shelves is as large as possible. Compute this maximum possible beauty.


-----Input-----

The first line contains two integers $n$ and $k$ ($1 \leq k \leq n \leq 50$) — the number of books and the number of shelves in the new office.

The second line contains $n$ integers $a_1, a_2, \ldots a_n$, ($0 < a_i < 2^{50}$) — the prices of the books in the order they stand on the old shelf.


-----Output-----

Print the maximum possible beauty of $k$ shelves in the new office.


-----Examples-----
Input
10 4
9 14 28 1 7 13 15 29 2 31

Output
24

Input
7 3
3 14 15 92 65 35 89

Output
64



-----Note-----

In the first example you can split the books as follows:

$$(9 + 14 + 28 + 1 + 7) \& (13 + 15) \& (29 + 2) \& (31) = 24.$$

In the second example you can split the books as follows:

$$(3 + 14 + 15 + 92) \& (65) \& (35 + 89) = 64.$$
"""

def calculate_maximum_beauty(n, k, book_prices):
    # Precompute the prefix sums for efficient range sum calculations
    sums = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n + 1):
            sums[i][j] = sums[i][j - 1] + book_prices[j - 1]

    class SearchProblem:
        def __init__(self, a, n, k):
            self.a = a
            self.n = n
            self.k = k
            self.maxResult = 0

        def search(self, currResult, currIndex, currLines):
            if currLines > 0 and currResult <= self.maxResult:
                return
            if currLines == self.k - 1:
                lastSum = sums[currIndex][self.n]
                currResult = currResult & lastSum
                if currResult > self.maxResult:
                    self.maxResult = currResult
                return
            for nextIndex in range(currIndex + 1, self.n + 1):
                currSum = sums[currIndex][nextIndex]
                if currLines == 0:
                    nextResult = currSum
                else:
                    nextResult = currResult & currSum
                self.search(nextResult, nextIndex, currLines + 1)

    problem = SearchProblem(book_prices, n, k)
    if k == 1:
        return sum(book_prices)
    problem.search(0, 0, 0)
    return problem.maxResult