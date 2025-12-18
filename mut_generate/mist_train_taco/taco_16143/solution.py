"""
QUESTION:
After battling Shikamaru, Tayuya decided that her flute is too predictable, and replaced it with a guitar. The guitar has 6 strings and an infinite number of frets numbered from 1. Fretting the fret number j on the i-th string produces the note a_{i} + j.

Tayuya wants to play a melody of n notes. Each note can be played on different string-fret combination. The easiness of performance depends on the difference between the maximal and the minimal indices of used frets. The less this difference is, the easier it is to perform the technique. Please determine the minimal possible difference.

For example, if a = [1, 1, 2, 2, 3, 3], and the sequence of notes is 4, 11, 11, 12, 12, 13, 13 (corresponding to the second example), we can play the first note on the first string, and all the other notes on the sixth string. Then the maximal fret will be 10, the minimal one will be 3, and the answer is 10 - 3 = 7, as shown on the picture.

<image>

Input

The first line contains 6 space-separated numbers a_{1}, a_{2}, ..., a_{6} (1 ≤ a_{i} ≤ 10^{9}) which describe the Tayuya's strings.

The second line contains the only integer n (1 ≤ n ≤ 100 000) standing for the number of notes in the melody.

The third line consists of n integers b_{1}, b_{2}, ..., b_{n} (1 ≤ b_{i} ≤ 10^{9}), separated by space. They describe the notes to be played. It's guaranteed that b_i > a_j for all 1≤ i≤ n and 1≤ j≤ 6, in other words, you can play each note on any string.

Output

Print the minimal possible difference of the maximal and the minimal indices of used frets.

Examples

Input


1 4 100 10 30 5
6
101 104 105 110 130 200


Output


0


Input


1 1 2 2 3 3
7
13 4 11 12 11 13 12


Output


7

Note

In the first sample test it is optimal to play the first note on the first string, the second note on the second string, the third note on the sixth string, the fourth note on the fourth string, the fifth note on the fifth string, and the sixth note on the third string. In this case the 100-th fret is used each time, so the difference is 100 - 100 = 0.

<image>

In the second test it's optimal, for example, to play the second note on the first string, and all the other notes on the sixth string. Then the maximal fret will be 10, the minimal one will be 3, and the answer is 10 - 3 = 7.

<image>
"""

from heapq import heapify, heapreplace

def minimal_fret_difference(a, n, b):
    # Sort the base notes of the strings in descending order
    a.sort(reverse=True)
    
    # Initialize the result to a large number
    res = float('inf')
    
    # Create a heap with the initial fret indices for each note
    heap = [(b[i] - a[0], i) for i in range(n)]
    heapify(heap)
    
    # Initialize the maximum fret index
    m = max(b) - a[0]
    
    # Count of how many times each note has been processed
    count = [0] * n
    
    while True:
        # Get the smallest fret index and its corresponding note index
        v, i = heap[0]
        
        # Update the result with the current difference
        res = min(res, m - v)
        
        # Increment the count for the current note
        count[i] += 1
        
        # If we have processed all 6 strings for this note, break the loop
        if count[i] == 6:
            break
        
        # Calculate the new fret index for the current note on the next string
        t = b[i] - a[count[i]]
        
        # Update the maximum fret index
        m = max(m, t)
        
        # Replace the smallest element in the heap with the new fret index
        heapreplace(heap, (t, i))
    
    return res