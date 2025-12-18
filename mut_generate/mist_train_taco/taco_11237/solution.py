"""
QUESTION:
Given a string s whose length is n and array queries of length q where each elements of queries is either of type 1 query or type 2 query which is explained ahead.
There are two types of query.
Query type 1 : ["1",ind,char]  "1" denotes this is type 1 query. In this query you have to change the character at index ind in s to character char.(Data type of ind,char is string in input)
Query Type 2: ["2",left,right,k]  "2" denotes this is type 2 query. In this query you have to return kth lexographically largest character  in the subtring of s (it is the kth largest character in sorted order , not the kth distinct character) starting from index left and ending at index right both left and right are inclusive. (Data type of left,right,k is string in input)
You have to perform each query in the same order as given in  queries and return an array res such that res array contains the answer for each type2 query in same order as it appeared in queries.
Note : 0 based indexing is used.
Example 1:
Input:
n=4
s="abab"
q=2
queries={{"1","2","d"},{"2","1","3","1"}}
Output: 
{"d"}
Explanation:
First query is of type 1 so after changing character at index 2 
to d  s becomes abdb . Now Second query is of type 2 in which 
the 1st(k=1) lexographically largest character is "d" in substring "bdb"(s[1:3]). So we 
returned a array with result of type 2 query {"d"}.
Example 2:
Input:
n=3
s="aaa"
q=3
queries={{"1","1","e"},{"1","2","c"},{"2","1","2","2"}}
Output:
{"c"}
Explanation:
After applying first two queries s becomes aec. Now for 
the last query which is a type 2 second largest character 
in subtring s starting from index 1 to ending at index 2 is "c".
Your Task:
You don't need to read input or print anything. Your task is to complete the function easyTask() which takes an integer n,string s,an integer q and an array queries which contains  queries of type1 and type2  respectively and returns an array res such that res array contains the answer for each type2 query in same order as it appeared in queries.
Expected Time Complexity: O(N+(Q*logN))
Expected Space Complexity: O(N)
Constraints:
1<=n<=5*10^4
1<=q<=10^5
0<=int(left)<=int(right)<=n-1
0<=int(index)<=n-1
1<=int(k)<=right-left+1
s and char contains lowercase english letters
The sum of n over all test cases won't exceed 5*10^4.
"""

from typing import List

class Fenwick:
    def __init__(self, n):
        self.T = [[0] * 26 for _ in range(n)]
        self.n = n
        self.F = lambda x: x & (x + 1)
        self.H = lambda x: x | (x + 1)

    def update(self, ind, c, delta):
        c = ord(c) - ord('a')
        while ind < self.n:
            self.T[ind][c] += delta
            ind = self.H(ind)

    def query(self, ind):
        result = [0] * 26
        while ind >= 0:
            for c in range(26):
                result[c] += self.T[ind][c]
            ind = self.F(ind) - 1
        return result

    def range_query(self, left, right):
        return [r - l for (r, l) in zip(self.query(right), self.query(left - 1))]

def process_queries(n: int, s: str, q: int, queries: List[List[str]]) -> List[str]:
    tree = Fenwick(n)
    s = list(s)
    for (ind, c) in enumerate(s):
        tree.update(ind, c, 1)
    res = []
    for query in queries:
        if query[0] == '1':
            (ind, char) = (int(query[1]), query[2])
            tree.update(ind, s[ind], -1)
            s[ind] = char
            tree.update(ind, s[ind], 1)
        else:
            (left, right, k) = (int(query[1]), int(query[2]), int(query[3]))
            counter = tree.range_query(left, right)
            for c in range(25, -1, -1):
                if k > counter[c]:
                    k -= counter[c]
                else:
                    res.append(chr(c + ord('a')))
                    break
    return res