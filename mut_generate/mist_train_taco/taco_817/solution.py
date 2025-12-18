"""
QUESTION:
There are total $N$ cars in a sequence with $ith$ car being assigned with an alphabet equivalent to the $ith$ alphabet of string $S$ . Chef has been assigned a task to calculate the total number of cars with alphabet having a unique even value in the given range X to Y (both inclusive)
. The value of an alphabet is simply its position in alphabetical order e.g.: a=1, b=2, c=3…
The chef will be given $Q$
such tasks having varying values of $X$ and $Y$
Note: string $S$ contains only lowercase alphabets

-----Input-----
First line of input contains a string $S$ of length $N$.
Second line contains an integer denoting no. of queries $Q$.
Next q lines contain two integers denoting values of $X$ and $Y$.

-----Output-----
For each query print a single integer denoting total number of cars with alphabet having a unique even value in the given range $X$ to $Y$.

-----Constraints-----
- $1 \leq n \leq 10^5$
- $1 \leq q \leq 10^5$

-----Example Input-----
bbccdd
5
1 2
3 4
5 6
1 6
2 5

-----Example Output-----
1
0
1
2
2

-----Explanation:-----
Example case 1: 
Query 1: range 1 to 2 contains the substring $"bb"$ where each character has a value of 2. Since we will only be considering unique even values, the output will be 1
"""

def count_unique_even_alphabets(S, queries):
    # List of even-valued alphabets
    even_alphabets = ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v', 'x', 'z']
    
    # Set of unique even-valued alphabets in the string S
    unique_even_alphabets = set(S).intersection(even_alphabets)
    
    results = []
    
    for (X, Y) in queries:
        # Convert to zero-based index
        start = X - 1
        end = Y
        
        # List of unique even-valued alphabets in the current range
        current_unique_even_alphabets = list(unique_even_alphabets)
        
        count = 0
        for i in range(start, end):
            if S[i] in current_unique_even_alphabets:
                count += 1
                current_unique_even_alphabets.remove(S[i])
            if not current_unique_even_alphabets:
                break
        
        results.append(count)
    
    return results