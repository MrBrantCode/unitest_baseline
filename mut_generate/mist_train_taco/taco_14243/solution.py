"""
QUESTION:
A weighted string is a string of lowercase English letters where each letter has a weight.  Character weights are $\mbox{1}$ to $26$ from $\class{ML__boldsymbol}{\boldsymbol{a}}$ to $z$ as shown below:

The weight of a string is the sum of the weights of its characters.  For example: 

A uniform string consists of a single character repeated zero or more times. For example, ccc and a are uniform strings, but bcb and cd are not.

Given a string, $\boldsymbol{\mathrm{~S~}}$, let $\mbox{U}$ be the set of weights for all possible uniform contiguous  substrings of string $\boldsymbol{\mathrm{~S~}}$. There will be $n$ queries to answer where each query consists of a single integer. Create a return array where for each query, the value is Yes if $\textit{query}[i]\in U$.  Otherwise, append No.

Note: The  $\in $ symbol denotes that $x[i]$ is an element of set $\mbox{U}$.Example $s=\text{'abbcccddd’}$ $queries=[1,7,5,4,15]$.  
Working from left to right, weights that exist are:
string  weighta     
  1b       2bb     
  4c       3cc      
  6ccc     9
   d       4 
   dd     8
   ddd     12
dddd    16

Now for each value in $queries$, see if it exists in the possible string weights.  The return array is ['Yes', 'No', 'No', 'Yes', 'No'].
Function Description  Complete the weightedUniformStrings function in the editor below. weightedUniformStrings has the following parameter(s): - string s: a string - int queries[n]: an array of integers   
Returns -   string[n]: an array of strings that answer the queries

Input FormatThe first line contains a string $\boldsymbol{\mathrm{~S~}}$, the original string. The second line contains an integer $n$, the number of queries. Each of the next $n$ lines contains an integer $\textit{queries}[i]$, the weight of a uniform subtring of $\boldsymbol{\mathrm{~S~}}$ that may or may not exist.

Constraints
$1\leq\textit{lengthofs},n\leq10^5$       
$1\leq\textit{queries[i]}\leq10^7$
$\boldsymbol{\mathrm{~S~}}$ will only contain lowercase English letters, ascii[a-z].

Sample Input0 
abccddde
6
1
3
12
5
9 
10

Sample Output0
Yes
Yes
Yes
Yes
No
No
Explanation 0
The weights of every possible uniform substring in the string abccddde are shown below:

We print Yes on the first four lines because the first four queries match weights of uniform substrings of $\boldsymbol{\mathrm{~S~}}$. We print No for the last two queries because there are no uniform substrings in $\boldsymbol{\mathrm{~S~}}$ that have those weights. 

Note that while de is a substring of $\boldsymbol{\mathrm{~S~}}$ that would have a weight of $\mbox{9}$, it is not a uniform substring.

 Note that we are only dealing with contiguous substrings. So ccc is not a substring of the string ccxxc.
Sample Input1
aaabbbbcccddd
5
9
7
8
12
5
Sample Output 1
Yes
No
Yes
Yes
No
"""

def weighted_uniform_strings(s, queries):
    # Initialize a set to store the weights of uniform substrings
    cost = set()
    prev = ''
    count = 0
    
    # Calculate the weights of all uniform substrings
    for i in s:
        if i != prev:
            prev = i
            count = 0
        count += 1
        weight = count * (ord(i) - ord('a') + 1)
        cost.add(weight)
    
    # Prepare the result list based on the queries
    result = []
    for query in queries:
        if query in cost:
            result.append("Yes")
        else:
            result.append("No")
    
    return result