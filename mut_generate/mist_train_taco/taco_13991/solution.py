"""
QUESTION:
The following graph G is called a Petersen graph and its vertices have been numbered from 0 to 9. Some letters have also been assigned to vertices of G, as can be seen from the following picture:

	Let's consider a walk W in graph G, which consists of L vertices W1, W2, ..., WL, such that Wi is connected with Wi + 1 for 1 ≤ i < L. A string S of L letters 'A'-'E' is realized by walk W if the sequence of letters written along W is equal to S. Vertices can be visited multiple times while walking along W.

For example, S = 'ABBECCD' is realized by W = (0, 1, 6, 9, 7, 2, 3).
Your task is to determine whether there is a walk W which realizes a given string S in graph G, and if so, find the lexicographically least such walk.

-----Input-----

	The first line of the input contains one integer T denoting the number of testcases to process.

	The only line of each testcase contains one string S. It is guaranteed that S only consists of symbols 'A'-'E'.

-----Output-----

	The output should contain exactly T lines, one line per each testcase in the order of their appearance. For each testcase, if there is no walk W which realizes S, then output -1. Otherwise, you should output the least lexicographical walk W which realizes S. Since all of the vertices are numbered from 0 to 9, then it can be encoded as a string consisting of symbols '0'-'9' (see the "Examples" section for more details).

-----Constraints-----
1 ≤ T ≤ 8;
1 ≤ |S| ≤ 100000(105).

-----Examples-----
Input:
2
AAB
AABE

Output:
501
-1
"""

def find_lexicographically_least_walk(S: str) -> str:
    let_to_num = {'A': [0, 5], 'B': [1, 6], 'C': [2, 7], 'D': [3, 8], 'E': [4, 9]}
    num_to_let = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'A', 6: 'B', 7: 'C', 8: 'D', 9: 'E'}
    connections = {
        0: (1, 4, 5), 1: (0, 2, 6), 2: (1, 3, 7), 3: (2, 4, 8), 4: (0, 3, 9),
        5: (0, 7, 8), 6: (1, 8, 9), 7: (2, 5, 9), 8: (3, 5, 6), 9: (4, 6, 7)
    }
    
    out_1, out_2 = [], []
    flag1, flag2 = True, True
    
    for c in range(len(S)):
        if c == 0:
            out_1.append(let_to_num[S[c]][0])
            out_2.append(let_to_num[S[c]][1])
        else:
            if flag1:
                conn_1 = set(connections[out_1[-1]])
                to_conn_1 = set(let_to_num[S[c]])
                if len(conn_1.intersection(to_conn_1)) == 0:
                    flag1 = False
                else:
                    out_1.extend(list(conn_1.intersection(to_conn_1)))
            if flag2:
                conn_2 = set(connections[out_2[-1]])
                to_conn_2 = set(let_to_num[S[c]])
                if len(conn_2.intersection(to_conn_2)) == 0:
                    flag2 = False
                else:
                    out_2.extend(list(conn_2.intersection(to_conn_2)))
            if not flag1 and not flag2:
                break
    
    if not flag1 and not flag2:
        return "-1"
    elif flag1 and not flag2:
        return ''.join(str(k) for k in out_1)
    elif flag2 and not flag1:
        return ''.join(str(k) for k in out_2)
    else:
        return min(''.join(str(k) for k in out_1), ''.join(str(k) for k in out_2))