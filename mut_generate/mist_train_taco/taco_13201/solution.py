"""
QUESTION:
You're researching friendships between groups of $n$ new college students where each student is distinctly numbered from $1$ to $n$. At the beginning of the semester, no student knew any other student; instead, they met and formed individual friendships as the semester went on. The friendships between students are:

Bidirectional. If student $\class{ML__boldsymbol}{\boldsymbol{a}}$ is friends with student $\boldsymbol{b}$, then student $\boldsymbol{b}$ is also friends with student $\class{ML__boldsymbol}{\boldsymbol{a}}$.
Transitive. If student $\class{ML__boldsymbol}{\boldsymbol{a}}$ is friends with student $\boldsymbol{b}$ and student $\boldsymbol{b}$ is friends with student $c$, then student $\class{ML__boldsymbol}{\boldsymbol{a}}$ is friends with student $c$. In other words, two students are considered to be friends even if they are only indirectly linked through a network of mutual (i.e., directly connected) friends. 

The purpose of your research is to find the maximum total value of a group's friendships, denoted by $total$. Each time a direct friendship forms between two students, you sum the number of friends that each of the $n$ students has and add the sum to $total$. 

You are given $\textit{q}$ queries, where each query is in the form of an unordered list of $m$ distinct direct friendships between $n$ students. For each query, find the maximum value of $total$ among all possible orderings of formed friendships and print it on a new line.

Input Format

The first line contains an integer, $\textit{q}$, denoting the number of queries. The subsequent lines describe each query in the following format:

The first line contains two space-separated integers describing the respective values of $n$ (the number of students) and $m$ (the number of distinct direct friendships).
Each of the $m$ subsequent lines contains two space-separated integers describing the respective values of $\boldsymbol{x}$ and $y$ (where $x\neq y$) describing a friendship between student $\boldsymbol{x}$ and student $y$.

Constraints

$1\leq q\leq16$  
$1\leq n\leq10^5$   
$1\leq m\leq\text{min}(\frac{n\cdot(n-1)}{2},2\times10^5)$  

Output Format

For each query, print the maximum value of $total$ on a new line.

Sample Input 0
1
5 4
1 2
3 2
4 2
4 3

Sample Output 0
32

Explanation 0

The value of $total$ is maximal if the students form the $m=4$ direct friendships in the following order:

Students $1$ and $2$ become friends: 

We then sum the number of friends that each student has to get $1+1+0+0+0=2$.

Students $2$ and $\begin{array}{c}4\end{array}$ become friends: 

We then sum the number of friends that each student has to get $2+2+0+2+0=6$.

Students $3$ and $\begin{array}{c}4\end{array}$ become friends: 

We then sum the number of friends that each student has to get $3+3+3+3+0=12$.

Students $3$ and $2$ become friends: 

We then sum the number of friends that each student has to get $3+3+3+3+0=12$.

When we add the sums from each step, we get $total=2+6+12+12=32$. We then print $32$ on a new line.
"""

def calculate_max_total_friendships(n, m, friendships):
    def grow(n):
        res = 0
        for i in range(1, n):
            res += i * (i + 1)
        return res

    def mark(x):
        z = x
        while z:
            z = z[0]
        if x is not z:
            x[0] = z
        return z

    def mark2(x):
        z = x
        while z and type(z) == list:
            z = z[0]
        if x is not z:
            x[0] = z
        return z

    work = [[] for i in range(n)]
    lost = 0
    for u, v in friendships:
        u -= 1
        v -= 1
        mu = mark(work[u])
        mv = mark(work[v])
        if mu is not mv:
            mu.append(mv)
        else:
            lost += 1

    no = 1
    dic = {}
    for i in range(n):
        z = mark2(work[i])
        if not z:
            z.append(no)
            z = no
            no += 1
            dic[z] = 1
        else:
            dic[z] += 1

    res = 0
    cur = 0
    for v in sorted(dic.values(), reverse=True):
        res += grow(v) + (v - 1) * cur
        cur += v * (v - 1)
    res += lost * cur
    return res