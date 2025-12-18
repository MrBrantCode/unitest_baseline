"""
QUESTION:
Chef's brother likes to put words in Chef's mouth.
Chef hates it about him of course.
He has decided to become extremely careful about what he speaks.
Fortunately, he knows how his brother transforms the words, that Chef uses.
He has decided to use only those words which remain the same even after his brother's transformation!

If Chef speaks an N letter word, his brother moves all the letters which are at even positions (assuming, numbering of positions starts from 1), to the beginning of the word; and the rest of the letters follow as they appeared in the word. Eg. abdef becomes beadf; cdcd becomes ddcc.

Chef wants to know how many words can he use, provided that each word is composed of exactly N lowercase letters of the English alphabet. They use an ancient language in Byteland, which allows all possible words within the above definition!

Input format

The first line contains the number T, the number of test cases. In the following lines, T test cases follow. Every test case is a single line, that contains a single positive integer, N,
which is the length of the words that Chef wants to use.

Output format

For each test case, print the number of words of length N that Chef can use; that is, number of words, which remain the same after brother's transformation. 
Since the result can be quite large, output the result modulo 1000000007.

------ Constraints ------ 
 
1 ≤ T ≤ 100

1 ≤ N ≤ 100000

----- Sample Input 1 ------ 
3
1
14
45
----- Sample Output 1 ------ 
26
456976
827063120
"""

def count_stable_words(n: int) -> int:
    mod = 1000000007
    
    visited = [False] * (n + 1)
    pos = []
    
    # Collect positions to be moved to the beginning
    for i in range(0, n + 1, 2):
        pos.append(i)
    
    # Collect remaining positions
    for i in range(1, n + 1, 2):
        pos.append(i)
    
    count = 0
    
    # Count the number of cycles in the permutation
    for i in range(1, n + 1):
        if not visited[i]:
            count += 1
            while not visited[i]:
                visited[i] = True
                i = pos[i]
    
    # Return the number of stable words modulo 1000000007
    return pow(26, count, mod)