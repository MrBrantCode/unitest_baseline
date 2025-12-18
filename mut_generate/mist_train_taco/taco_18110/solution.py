"""
QUESTION:
The Berland University is preparing to celebrate the 256-th anniversary of its founding! A specially appointed Vice Rector for the celebration prepares to decorate the campus. In the center of the campus n ice sculptures were erected. The sculptures are arranged in a circle at equal distances from each other, so they form a regular n-gon. They are numbered in clockwise order with numbers from 1 to n.

The site of the University has already conducted a voting that estimated each sculpture's characteristic of ti — the degree of the sculpture's attractiveness. The values of ti can be positive, negative or zero.

When the university rector came to evaluate the work, he said that this might be not the perfect arrangement. He suggested to melt some of the sculptures so that: 

  * the remaining sculptures form a regular polygon (the number of vertices should be between 3 and n), 
  * the sum of the ti values of the remaining sculptures is maximized. 



Help the Vice Rector to analyze the criticism — find the maximum value of ti sum which can be obtained in this way. It is allowed not to melt any sculptures at all. The sculptures can not be moved.

Input

The first input line contains an integer n (3 ≤ n ≤ 20000) — the initial number of sculptures. The second line contains a sequence of integers t1, t2, ..., tn, ti — the degree of the i-th sculpture's attractiveness ( - 1000 ≤ ti ≤ 1000). The numbers on the line are separated by spaces.

Output

Print the required maximum sum of the sculptures' attractiveness.

Examples

Input

8
1 2 -3 4 -5 5 2 3


Output

14


Input

6
1 -2 3 -4 5 -6


Output

9


Input

6
1 2 3 4 5 6


Output

21

Note

In the first sample it is best to leave every second sculpture, that is, leave sculptures with attractivenesses: 2, 4, 5 и 3.
"""

def maximize_sculpture_attractiveness(n, t):
    max_sum = 0
    
    # Calculate the sum of all sculptures initially
    for i in range(n):
        max_sum += t[i]
    
    # Check for all possible regular polygons that can be formed
    for i in range(2, n):
        if n % i == 0 and n // i >= 3:
            for j in range(i):
                current_sum = 0
                x = j
                while x < n:
                    current_sum += t[x]
                    x += i
                if current_sum > max_sum:
                    max_sum = current_sum
    
    return max_sum