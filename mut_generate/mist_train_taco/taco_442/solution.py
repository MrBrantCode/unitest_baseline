"""
QUESTION:
Teddy and Freddy are two friends. Teddy has a pile of strings of size $N$. Each string $Si$ in the pile has length less or equal to $100$ ($len(Si) \leq 100$). 
Teddy and Freddy like playing with strings. Teddy gives Freddy a string $B$ of size $M$.
Teddy and Freddy like playing with strings. Teddy gives Freddy a string $B$ of size $M$.
He asks Freddy to find the count of the unique substrings of $B$ present in pile of strings of size $N$.
Freddy is busy with the some task, so he asks for your help.Help Freddy by giving the unique substrings of $B$ present in pile of strings of size $N$.
Note: The substrings having same permutation of characters are considered same.

-----Input:-----
- First line will contain $N$, number of strings. Then the strings follow. 
- Next $N$ lines will contain a string 
- $N+2$ line contains the $M$ - length of string B
- Following line contains the string B

-----Output:-----
For each testcase, output in a single line number of unique strings of B.

-----Constraints-----
- $1 \leq N \leq 100$
- $2 \leq len(Si) \leq 100$
- $2 \leq M \leq 100$

-----Sample Input:-----
4
a
abc 
abcd
abcde
5
aaaaa

-----Sample Output:-----
1

-----Sample Input:-----
4
a
aa
aaa
aaaa
5
aaaaa

-----Sample Output:-----
4

-----EXPLANATION:-----
TestCase 1: Only substring of $aaaaa$ that is present in the pile of strings is $a$. So the answer is 1
"""

def count_unique_substrings_in_pile(pile, B):
    # Generate all possible substrings of B
    substrings = [B[i:j] for i in range(len(B)) for j in range(i + 1, len(B) + 1)]
    
    # Remove duplicates by converting to a set and back to a list
    unique_substrings = list(dict.fromkeys(substrings))
    
    # Count how many unique substrings are present in the pile
    count = 0
    for substring in unique_substrings:
        if substring in pile:
            count += 1
    
    return count