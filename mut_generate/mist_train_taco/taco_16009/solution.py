"""
QUESTION:
Jack is the most intelligent student in the class.To boost his intelligence,his class teacher gave him a problem named "Substring Count".

Problem :
His Class teacher gave him n strings numbered from 1 to n which consists of only lowercase letters (each having length not more than 10) and then ask Q questions related to the given strings.

Each question is described by the 2 integers L,R and a string str,Now his teacher wants to know how many strings numbered from L to R contains str as a substrings.  

As expected, Jack solved this problem with in a minute but he failed to solve it efficiently.Now ,its your turn to teach him.How to do it efficiently?? and save him from punishment.

INPUT
First line of input contains a single integer n denoting the number of strings given by class teacher to jack.Next n lines of input contains n strings (one per line).Next line fo input contains a single integer Q denoting the number of questions asked by his teacher.next Q lines of input contains Q question (one per line) as explained above.

OUTPUT
print the correct answer for each of the question asked by his teacher.

CONSTRAINTS
1 ≤ n ≤ 10000
1 ≤ strlen(str) ≤ 10
1 ≤ Q ≤ 5*10^5
1 ≤ L,R ≤ n  

NOTE: strings consist of only lower case characters 

SAMPLE INPUT
3
code
coder
coding
2
1 3 code
1 3 co

SAMPLE OUTPUT
2 
3

Explanation

Q1:: code coder coding only two out of 3 strings contain cod as substring
Q2:: code coder coding all the 3 strings contain co as substring
"""

def count_substring_occurrences(n, strings, queries):
    from collections import defaultdict

    def binary_search(temp, i, j, k):
        if k <= temp[i]:
            return i - 1
        while j - i > 1:
            mid = (i + j) // 2
            if temp[mid] < k:
                i = mid
            elif temp[mid] > k:
                j = mid - 1
            else:
                j = mid - 1
        if temp[j] < k:
            return j
        if temp[i] < k:
            return i
        return i - 1

    # Preprocess the strings to create a dictionary of substrings
    d = defaultdict(list)
    for idx, s in enumerate(strings):
        length = len(s)
        check = set()
        for j in range(length):
            for k in range(j + 1, length + 1):
                temp = s[j:k]
                if temp not in check:
                    d[temp].append(idx)
                    check.add(temp)

    results = []
    for (L, R, s) in queries:
        L = int(L) - 1
        R = int(R) - 1
        if s not in d:
            results.append(0)
        else:
            temp = d[s]
            length = len(temp)
            left = binary_search(temp, 0, length - 1, L)
            right = binary_search(temp, 0, length - 1, R + 1)
            results.append(right - left)

    return results