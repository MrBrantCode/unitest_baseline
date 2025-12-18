"""
QUESTION:
Given a positive integer n, write a function get_matrix_triples(n) to calculate the total number of unique triples (a{i}, a{j}, a{k}) within the array a of length n, where a{i} = i * i - i + 1, i < j < k, and the sum a[i] + a[j] + a[k] is divisible by 3. The function should have a time complexity of O(n).
"""

def get_matrix_triples(n):
    a = [i * i - i + 1 for i in range(n)]
    count = [0, 0, 0]
    pairs = [0, 0, 0]
    triples = 0

    for i in a:
        count[i % 3] += 1

    for j in range(3):
        for k in range(j + 1, 3):
            pairs[k] += count[j] * count[k]
        triples += (count[j] * (count[j] - 1) * (count[j] - 2)) // 6

    triples += pairs[0] + 2 * (pairs[1] + pairs[2])

    return triples