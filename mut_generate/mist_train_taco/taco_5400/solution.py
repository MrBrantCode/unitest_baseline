"""
QUESTION:
It's year 2018 and it's Christmas time! Before going for vacations, students of Hogwarts School of Witchcraft and Wizardry had their end semester exams.
$N$ students attended the semester exam. Once the exam was over, their results were displayed as either "Pass" or "Fail" behind their magic jacket which they wore. A student cannot see his/her result but can see everyone else's results. Each of $N$ students count the number of passed students they can see.
Given the number of "Pass" verdicts that each of the $N$ students counted, we have to figure out conclusively, the number of students who failed, or report that there is some inconsistency or that we cannot be sure.

-----Input:-----
- First line will contain $T$, number of testcases. Then the testcases follow. 
- The first line of each test case will contain $N$, representing the number of students who attended the exam.
- Next line contains  $N$ spaced integers representing the number of "Pass" counted by each of the $N$ students.

-----Output:-----
- For each test case, output the answer in a single line. 
- If the counts reported by the students are not consistent with each other or if it's not possible to predict the number of failed students from the given input, then print -1.

-----Constraints-----
- $1 \leq T \leq 50$
- $1 \leq N \leq 10^{5}$
- $0 \leq$ Count given by each Student $\leq 10^{5}$

-----Sample Input:-----
1
4
3 2 2 2

-----Sample Output:-----
1

-----EXPLANATION:-----
There are 4 students, and they counted the number of passed students as 3,2,2,2. The first student can see that all others have passed, and all other students can see only 2 students who have passed. Hence, the first student must have failed, and others have all passed. Hence, the answer is 1.
"""

def determine_failed_students(test_cases):
    results = []
    
    for case in test_cases:
        N, counts = case
        unique_counts = set(counts)
        
        if N == 1 or len(unique_counts) > 2:
            results.append(-1)
            continue
        
        if len(unique_counts) == 1:
            x = unique_counts.pop()
            if x == 0:
                results.append(N)
            elif x == N - 1:
                results.append(0)
            else:
                results.append(-1)
            continue
        
        x, y = sorted(unique_counts)
        x_count = counts.count(x)
        y_count = counts.count(y)
        
        if x_count == y and x_count == x + 1:
            results.append(y_count)
        else:
            results.append(-1)
    
    return results