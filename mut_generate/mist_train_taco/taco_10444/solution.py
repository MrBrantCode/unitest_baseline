"""
QUESTION:
The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want. 

For example:

from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i

This prints:

('python', ['awesome', 'language'])
('something-else', ['not relevant'])

In this challenge, you will be given $2$ integers, $n$ and $m$. There are $n$ words, which might repeat, in word group $\mbox{A}$. There are $m$ words belonging to word group $\mbox{B}$. For each  $m$ words, check whether the word has appeared in group $\mbox{A}$ or not. Print the indices of each occurrence of $m$ in group $\mbox{A}$. If it does not appear, print $-1$.

Example  

Group A contains 'a', 'b', 'a'
Group B contains 'a', 'c'

For the first word in group B, 'a', it appears at positions $\mbox{I}$ and $3$ in group A.
The second word, 'c', does not appear in group A, so print $-1$.

Expected output:

1 3
-1

Input Format

The first line contains integers, $n$ and $m$ separated by a space. 

The next $n$ lines contains the words belonging to group $\mbox{A}$. 

The next $m$ lines contains the words belonging to group $\mbox{B}$.

Constraints

$1\leq n\leq10000$ 

$1\leq m\leq100$ 

$1\leq\textit{length of each word in the input}\leq100$

Output Format

Output $m$ lines. 

The $i^{\mbox{th}}$ line should contain the $\mbox{I}$-indexed positions of the occurrences of the $i^{\mbox{th}}$ word separated by spaces. 

Sample Input
STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b

Sample Output
1 2 4
3 5

Explanation

'a' appeared $3$ times in positions $\mbox{I}$, $2$ and $\begin{array}{c}A\end{array}$. 

 'b' appeared $2$ times in positions $3$ and $5$. 

In the sample problem, if 'c' also appeared in word group $\mbox{B}$, you would print $-1$.
"""

from collections import defaultdict

def find_word_occurrences(group_A, group_B):
    word_indices = defaultdict(list)
    
    # Populate the defaultdict with indices of words in group A
    for index, word in enumerate(group_A):
        word_indices[word].append(str(index + 1))
    
    # Prepare the result list based on group B
    result = []
    for word in group_B:
        if word in word_indices:
            result.append(' '.join(word_indices[word]))
        else:
            result.append('-1')
    
    return result