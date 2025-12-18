"""
QUESTION:
problem

Five students, Taro, Jiro, Saburo, Shiro, and Hanako, participated in the JOI High School class.

In this class, a final exam was conducted. All five people took the final exam. For students with a final exam score of 40 or higher, the final exam score was used as is. All students with a final exam score of less than 40 received supplementary lessons and scored 40 points.

Create a program that calculates the average score of the five students' grades given the final exam scores of the five students.





Example

Input

10
65
100
30
95


Output

68
"""

def calculate_average_score(scores):
    adjusted_scores = []
    for score in scores:
        if score < 40:
            adjusted_scores.append(40)
        else:
            adjusted_scores.append(score)
    return int(sum(adjusted_scores) / 5)