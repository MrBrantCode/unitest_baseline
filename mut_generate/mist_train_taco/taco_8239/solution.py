"""
QUESTION:
Geek has a list Li containing (not necessarily distinct) N words and Q queries. Each query consists of a string x. For each query, find how many strings in the List Li has the string x as its prefix. 
Example 1:
Input: 
N = 5, Q = 5
li[] = {'abracadabra', 'geeksforgeeks', 
      'abracadabra', 'geeks', 'geeksthrill'}
query[] = {'abr', 'geeks', 'geeksforgeeks', 
         'ge', 'gar'}
Output: 2 3 1 3 0
Explaination: 
Query 1: The string 'abr' is prefix of 
two 'abracadabra'. 
Query 2: The string 'geeks' is prefix of three 
strings 'geeksforgeeks', 'geeks' and 'geeksthrill'. 
Query 3: The string 'geeksforgeeks' is prefix 
of itself present in li. 
Query 4: The string 'ge' also is prefix of three 
strings 'geeksforgeeeks', 'geeks', 'geeksthrill'. 
Query 5: The string 'gar' is not a prefix of any 
string in li.
Your Task:
You do not need to read input or print anything. Your task is to complete the function prefixCount() which takes N, Q, li[] and query[] as input parameters and returns a list containing the count of prefixes for each query. 
Expected Time Complexity: O(Q*x) + O(N*L) Where Q is the number of queries, x is the longest word in the query, N = number of words inserted in Trie and L = length of longest word inserted in Trie.
Expected Auxiliary Space: O(N*List [i])
Constraints:
1 ≤ N ≤ 3 x 10^{4}
1 ≤ Q ≤ 10^{4}
1 ≤ |li[i]|, |x| ≤ 100
"""

def prefix_count(N, Q, li, query):
    dic = {}
    for word in li:
        strr = ''
        for char in word:
            strr += char
            if strr not in dic:
                dic[strr] = 1
            else:
                dic[strr] += 1
    ans = []
    for q in query:
        if q in dic:
            ans.append(dic[q])
        else:
            ans.append(0)
    return ans