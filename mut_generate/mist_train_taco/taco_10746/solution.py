"""
QUESTION:
Volodya has recently visited a very odd town. There are N tourist attractions in the town and every two of them are connected by a bidirectional road. Each road has some travel price (natural number) assigned to it and all prices are distinct. But the most striking thing about this town is that each city sightseeing tour has the same total price! That is, if we choose any city sightseeing tour — a cycle which visits every attraction exactly once — the sum of the costs of the tour roads is independent of the tour. Volodya is curious if you can find such price system with all road prices not greater than 1000.

Input

Input contains just one natural number (3 ≤ N ≤ 20) — the number of town attractions.

Output

Output should contain N rows containing N positive integer numbers each — the adjacency matrix of the prices graph (thus, j-th number in i-th row should be equal to the price of the road between the j-th and the i-th attraction). Diagonal numbers should be equal to zero. All numbers should not be greater than 1000. All prices should be positive and pairwise distinct. If there are several solutions, output any of them.

Examples

Input

3


Output

0 3 4 
3 0 5 
4 5 0
"""

def generate_tourist_attraction_matrix(n):
    """
    Generates an adjacency matrix for a graph of n tourist attractions where each cycle visiting all attractions exactly once has the same total price.

    Parameters:
    n (int): The number of tourist attractions (3 ≤ n ≤ 20).

    Returns:
    list: A 2D list representing the adjacency matrix of the graph.
    """
    
    def constructRow(n):
        can = [1 for i in range(1001)]
        b = [0 for i in range(n + 1)]
        b[2] = 1
        b[3] = 2
        can[1] = 0
        can[2] = 0
        for k in range(4, n + 1):
            b[k] = b[k - 1] + 1
            while not can[b[k]]:
                b[k] += 1
            can[b[k]] = 0
            for i in range(2, k):
                for p in range(2, k):
                    can[b[k] + b[p] - b[i]] = 0
        return b

    def constructMatrix(b, n):
        can = [1 for i in range(1001)]
        for i in range(2, n + 1):
            for j in range(2, n + 1):
                for p in range(2, n + 1):
                    can[b[2] + b[3] + b[p] - b[i] - b[j]] = 0
        x = 1
        while not can[x]:
            x += 1
        a = [[0 for j in range(n + 1)] for i in range(n + 1)]
        for i in range(n + 1):
            a[1][i] = a[i][1] = b[i]
        for i in range(2, n + 1):
            for j in range(i + 1, n + 1):
                a[i][j] = a[j][i] = b[i] + b[j] + x - b[2] - b[3]
        return a

    b = constructRow(n)
    a = constructMatrix(b, n)
    
    # Convert the matrix to the required format (0-indexed and without the extra row/column)
    result = [[a[i][j] for j in range(1, n + 1)] for i in range(1, n + 1)]
    
    return result