"""
QUESTION:
After the educational reform Polycarp studies only two subjects at school, Safety Studies and PE (Physical Education). During the long months of the fourth term, he received n marks in them. When teachers wrote a mark in the journal, they didn't write in what subject the mark was for, they just wrote the mark.

Now it's time to show the journal to his strict parents. Polycarp knows that recently at the Parent Meeting the parents were told that he received a Safety Studies marks and b PE marks (a + b = n). Now Polycarp wants to write a subject's name in front of each mark so that: 

  * there are exactly a Safety Studies marks, 
  * there are exactly b PE marks, 
  * the total average score in both subjects is maximum. 



An average subject grade is the sum of all marks in it, divided by the number of them. Of course, the division is performed in real numbers without rounding up or down. Polycarp aims to maximize the x1 + x2, where x1 is the average score in the first subject (Safety Studies), and x2 is the average score in the second one (Physical Education).

Input

The first line contains an integer n (2 ≤ n ≤ 105), n is the number of marks in Polycarp's Journal. The second line contains two positive integers a, b (1 ≤ a, b ≤ n - 1, a + b = n). The third line contains a sequence of integers t1, t2, ..., tn (1 ≤ ti ≤ 5), they are Polycarp's marks.

Output

Print the sequence of integers f1, f2, ..., fn, where fi (1 ≤ fi ≤ 2) is the number of a subject to which the i-th mark should be attributed. If there are several possible solutions, then print such that the sequence f1, f2, ..., fn is the smallest lexicographically.

The sequence p1, p2, ..., pn is lexicographically less than q1, q2, ..., qn if there exists such j (1 ≤ j ≤ n) that pi = qi for all 1 ≤ i < j, аnd pj < qj.

Examples

Input

5
3 2
4 4 5 4 4


Output

1 1 2 1 2 

Input

4
2 2
3 5 4 5


Output

1 1 2 2 

Input

6
1 5
4 4 4 5 4 4


Output

2 2 2 1 2 2 

Note

In the first sample the average score in the first subject is equal to 4, and in the second one — to 4.5. The total average score is 8.5.
"""

from operator import itemgetter
from collections import defaultdict

def maximize_average_scores(n, a, b, marks):
    # Enumerate the marks with their indices
    enumerated_marks = list(enumerate(marks, 0))
    
    # Sort the enumerated marks by their values in descending order
    sorted_marks = sorted(enumerated_marks, key=itemgetter(1), reverse=True)
    
    # Initialize the result list
    result = [0] * n
    
    # Helper function to find the minimum of two numbers
    def find_min(num1, num2):
        return num1 if num1 < num2 else num2
    
    # If the number of marks for both subjects is the same
    if a == b:
        for i in range(a):
            result[i] = 1
        for j in range(a, n):
            if result[j] == 0:
                result[j] = 2
    # If the number of Safety Studies marks is greater than PE marks
    elif a > b:
        dicta = defaultdict(list)
        for i in range(n):
            dicta[sorted_marks[i][1]].append(sorted_marks[i][0])
        for j in range(b, n):
            result[dicta[sorted_marks[j][1]][0]] = 1
            dicta[sorted_marks[j][1]].pop(0)
        for k in range(b):
            result[dicta[sorted_marks[k][1]][0]] = 2
            dicta[sorted_marks[k][1]].pop(0)
    # If the number of PE marks is greater than Safety Studies marks
    else:
        min_value = find_min(a, b)
        if min_value == a:
            second_range = b
            val = 1
        else:
            second_range = a
            val = 2
        for i in range(min_value):
            result[sorted_marks[i][0]] = val
        if val == 1:
            new_val = 2
        else:
            new_val = 1
        for j in range(min_value, n):
            result[sorted_marks[j][0]] = new_val
    
    return result