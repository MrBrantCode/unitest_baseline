"""
QUESTION:
One company of IT City decided to create a group of innovative developments consisting from 5 to 7 people and hire new employees for it. After placing an advertisment the company received n resumes. Now the HR department has to evaluate each possible group composition and select one of them. Your task is to count the number of variants of group composition to evaluate.


-----Input-----

The only line of the input contains one integer n (7 ≤ n ≤ 777) — the number of potential employees that sent resumes.


-----Output-----

Output one integer — the number of different variants of group composition.


-----Examples-----
Input
7

Output
29
"""

def count_group_composition_variants(n):
    def c(n, k):
        ans = 1
        for i in range(k):
            ans *= n - i
        for i in range(k):
            ans //= i + 1
        return ans
    
    return c(n, 5) + c(n, 6) + c(n, 7)