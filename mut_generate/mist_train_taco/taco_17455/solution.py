"""
QUESTION:
A Professor of Physics gave projects to the students of his class. The students have to form a team of two for doing the project. The professor left the students to decide the teams. The number of students in a class will be even.

Each student has a knowledge level. It tells how much knowledge each student has. The knowledge level of a team is the sum of the knowledge levels of both the students.

The students decide to form groups such that the difference between the team with highest knowledge and the one with lowest knowledge is minimum.

Input

First line of the input will contain number of test cases t; In the next t lines the first number is n the number of students in the class followed by n integers denoting the knowledge levels of the n students

Output

Your output should be a single line containing the lowest possible difference between the team with highest knowledge and the one with lowest knowledge.

SAMPLE INPUT
2
4 2 6 4 3
6 1 1 1 1 1 1

SAMPLE OUTPUT
1
0

Explanation

Input Constraints are

1 ≤ t ≤ 100
1 ≤ n ≤ 100
1 ≤ knowledge level ≤ 10000
"""

def calculate_min_knowledge_difference(test_cases):
    results = []
    
    for case in test_cases:
        n = case[0]
        knowledge_levels = sorted(case[1:])
        
        l = n // 2
        list3 = knowledge_levels[:l]
        list4 = knowledge_levels[l:]
        
        max1 = 0
        min1 = 9999
        
        for i in range(l):
            sum_knowledge = list3[i] + list4[-i-1]
            if max1 < sum_knowledge:
                max1 = sum_knowledge
            if min1 > sum_knowledge:
                min1 = sum_knowledge
        
        diff = max1 - min1
        results.append(diff)
    
    return results