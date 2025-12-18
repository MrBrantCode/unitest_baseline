"""
QUESTION:
Entrance Examination

The International Competitive Programming College (ICPC) is famous for its research on competitive programming. Applicants to the college are required to take its entrance examination.

The successful applicants of the examination are chosen as follows.

* The score of any successful applicant is higher than that of any unsuccessful applicant.
* The number of successful applicants n must be between nmin and nmax, inclusive. We choose n within the specified range that maximizes the gap. Here, the gap means the difference between the lowest score of successful applicants and the highest score of unsuccessful applicants.
* When two or more candidates for n make exactly the same gap, use the greatest n among them.



Let's see the first couple of examples given in Sample Input below. In the first example, nmin and nmax are two and four, respectively, and there are five applicants whose scores are 100, 90, 82, 70, and 65. For n of two, three and four, the gaps will be 8, 12, and 5, respectively. We must choose three as n, because it maximizes the gap.

In the second example, nmin and nmax are two and four, respectively, and there are five applicants whose scores are 100, 90, 80, 75, and 65. For n of two, three and four, the gap will be 10, 5, and 10, respectively. Both two and four maximize the gap, and we must choose the greatest number, four.

You are requested to write a program that computes the number of successful applicants that satisfies the conditions.

Input

The input consists of multiple datasets. Each dataset is formatted as follows.

> m nmin nmax
>  P1
>  P2
>  ...
>  Pm
>

The first line of a dataset contains three integers separated by single spaces. m represents the number of applicants, nmin represents the minimum number of successful applicants, and nmax represents the maximum number of successful applicants. Each of the following m lines contains an integer Pi, which represents the score of each applicant. The scores are listed in descending order. These numbers satisfy 0 < nmin < nmax < m ≤ 200, 0 ≤ Pi ≤ 10000 (1 ≤ i ≤ m) and Pnmin > Pnmax+1. These ensure that there always exists an n satisfying the conditions.

The end of the input is represented by a line containing three zeros separated by single spaces.

Output

For each dataset, output the number of successful applicants in a line.

Sample Input


5 2 4
100
90
82
70
65
5 2 4
100
90
80
75
65
3 1 2
5000
4000
3000
4 2 3
10000
10000
8000
8000
4 2 3
10000
10000
10000
8000
5 2 3
100
80
68
60
45
0 0 0


Output for the Sample Input


3
4
2
2
3
2






Example

Input

5 2 4
100
90
82
70
65
5 2 4
100
90
80
75
65
3 1 2
5000
4000
3000
4 2 3
10000
10000
8000
8000
4 2 3
10000
10000
10000
8000
5 2 3
100
80
68
60
45
0 0 0


Output

3
4
2
2
3
2
"""

def find_successful_applicants(m, nmin, nmax, scores):
    max_gap = -1
    best_n = nmin
    
    for n in range(nmin, nmax + 1):
        gap = scores[n - 1] - scores[n]
        if gap > max_gap:
            max_gap = gap
            best_n = n
        elif gap == max_gap:
            best_n = n
    
    return best_n