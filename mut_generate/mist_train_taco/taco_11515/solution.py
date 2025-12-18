"""
QUESTION:
You will be given a contest schedule for D days. For each d=1,2,\ldots,D, calculate the satisfaction at the end of day d.



Input

Input is given from Standard Input in the form of the input of Problem A followed by the output of Problem A.


D
c_1 c_2 \cdots c_{26}
s_{1,1} s_{1,2} \cdots s_{1,26}
\vdots
s_{D,1} s_{D,2} \cdots s_{D,26}
t_1
t_2
\vdots
t_D


* The constraints and generation methods for the input part are the same as those for Problem A.
* For each d, t_d is an integer satisfying 1\leq t_d \leq 26, and your program is expected to work correctly for any value that meets the constraints.



Output

Let v_d be the satisfaction at the end of day d. Print D integers v_d to Standard Output in the following format:


v_1
v_2
\vdots
v_D

Output

Let v_d be the satisfaction at the end of day d. Print D integers v_d to Standard Output in the following format:


v_1
v_2
\vdots
v_D

Example

Input

5
86 90 69 51 2 96 71 47 88 34 45 46 89 34 31 38 97 84 41 80 14 4 50 83 7 82
19771 12979 18912 10432 10544 12928 13403 3047 10527 9740 8100 92 2856 14730 1396 15905 6534 4650 11469 3628 8433 2994 10899 16396 18355 11424
6674 17707 13855 16407 12232 2886 11908 1705 5000 1537 10440 10711 4917 10770 17272 15364 19277 18094 3929 3705 7169 6159 18683 15410 9092 4570
6878 4239 19925 1799 375 9563 3445 5658 19857 11401 6997 6498 19933 3848 2426 2146 19745 16880 17773 18359 3921 14172 16730 11157 5439 256
8633 15862 15303 10749 18499 7792 10317 5901 9395 11433 3514 3959 5202 19850 19469 9790 5653 784 18500 10552 17975 16615 7852 197 8471 7452
19855 17918 7990 10572 4333 438 9140 9104 12622 4985 12319 4028 19922 12132 16259 17476 2976 547 19195 19830 16285 4806 4471 9457 2864 2192
1
17
13
14
13


Output

18398
35037
51140
65837
79325
"""

def calculate_satisfaction(D, c, s, t):
    d = [0] * 26  # Initialize the decrease array for each contest type
    v = [0] * (D + 1)  # Initialize the satisfaction array
    
    for i in range(D):
        contest_type = t[i] - 1  # Convert to 0-based index
        v[i] = s[i][contest_type]  # Satisfaction gain on day i
        d[contest_type] = -1  # Reset the decrease for the contest type held on day i
        
        sb = 0
        for j in range(26):
            d[j] += 1  # Increase the decrease for all contest types
            sb += d[j] * c[j]  # Calculate the total decrease in satisfaction
        
        if i > 0:
            v[i] += v[i - 1]  # Add the previous day's satisfaction
        v[i] -= sb  # Subtract the total decrease in satisfaction
    
    return v[:D]  # Return the satisfaction values for each day