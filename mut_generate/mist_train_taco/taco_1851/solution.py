"""
QUESTION:
At the school where the twins Ami and Mami attend, the summer vacation has already begun, and a huge amount of homework has been given this year as well. However, the two of them were still trying to go out without doing any homework today. It is obvious that you will see crying on the last day of summer vacation as it is, so you, as a guardian, decided not to leave the house until you finished your homework of reading impressions today with your heart as a demon.

Well-prepared you have already borrowed all the assignment books from the library. However, according to library rules, only one book is borrowed for each book. By the way, for educational reasons, I decided to ask them to read all the books and write their impressions without cooperating with each other. In addition, since the deadline for returning books is near, I decided to have them finish reading all the books as soon as possible. And you decided to think about how to do your homework so that you can finish your homework as soon as possible under those conditions. Here, the time when both the twins finish their work is considered as the time when they finish reading the book and the time when they finish their homework.

Since there is only one book for each book, two people cannot read the same book at the same time. In addition, due to adult circumstances, once you start reading a book, you cannot interrupt it, and once you start writing an impression about a book, you cannot interrupt it. Of course, I can't write my impressions about a book I haven't read. Since Ami and Mami are twins, the time it takes to read each book and the time it takes to write an impression are common to both of them.

For example, suppose that there are three books, and the time it takes to read each book and the time it takes to write an impression are as follows.

| Time to read a book | Time to write an impression
--- | --- | ---
Book 1 | 5 | 3
Book 2 | 1 | 2
Book 3 | 1 | 2



In this case, if you proceed with your homework as shown in Figure C-1, you can finish reading all the books in time 10 and finish your homework in time 15. In the procedure shown in Fig. C-2, the homework is completed in time 14, but it cannot be adopted this time because the time to finish reading the book is not the shortest. Also, as shown in Fig. C-3, two people cannot read the same book at the same time, interrupt reading of a book as shown in Fig. C-4, or write an impression of a book that has not been read.

<image>

Figure C-1: An example of how to get the homework done in the shortest possible time

<image>

Figure C-2: An example where the time to finish reading a book is not the shortest

<image>

Figure C-3: An example of two people reading the same book at the same time

<image>

Figure C-4: An example of writing an impression of a book that has not been read or interrupting work.

Considering the circumstances of various adults, let's think about how to proceed so that the homework can be completed as soon as possible for the twins who want to go out to play.

Input

The input consists of multiple datasets. The format of each data set is as follows.


N
r1 w1
r2 w2
...
rN wN


N is an integer representing the number of task books, and can be assumed to be 1 or more and 1,000 or less.

The following N lines represent information about the task book. Each line contains two integers separated by spaces, ri (1 ≤ ri ≤ 1,000) is the time it takes to read the i-th book, and wi (1 ≤ wi ≤ 1,000) is the impression of the i-th book. Represents the time it takes to write.

N = 0 indicates the end of input. This is not included in the dataset.

Output

For each dataset, output the minimum time to finish writing all the impressions on one line when the time to finish reading all the books by two people is minimized.

Sample Input


Four
1 1
3 1
4 1
twenty one
3
5 3
1 2
1 2
1
1000 1000
Ten
5 62
10 68
15 72
20 73
25 75
30 77
35 79
40 82
45 100
815 283
6
74 78
53 55
77 77
12 13
39 42
1 1
0


Output for Sample Input


14
15
3000
2013
522






Example

Input

4
1 1
3 1
4 1
2 1
3
5 3
1 2
1 2
1
1000 1000
10
5 62
10 68
15 72
20 73
25 75
30 77
35 79
40 82
45 100
815 283
6
74 78
53 55
77 77
12 13
39 42
1 1
0


Output

14
15
3000
2013
522
"""

def calculate_minimum_homework_time(n, books):
    if n == 0:
        return 0
    
    read_t = sum(r for r, w in books)
    write_t = sum(w for r, w in books)
    
    books = sorted(books)
    
    if books[-1][0] <= read_t // 2:
        return read_t + write_t
    
    sukima = books[-1][0] - (read_t - books[-1][0])
    dp = [[0 for _ in range(sukima + 1)] for _ in range(n)]
    
    for i in range(1, n):
        for j in range(1, sukima + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - books[i - 1][1]] + books[i - 1][1] if j - books[i - 1][1] >= 0 else 0)
    
    return read_t + write_t + sukima - dp[-1][-1]