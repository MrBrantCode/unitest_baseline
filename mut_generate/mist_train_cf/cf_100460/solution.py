"""
QUESTION:
Calculate the total time taken by a teacher to explain missed solutions and give extra problems, and the total time taken by a student to solve extra problems. 

Write a function `calculate_time` that takes two arguments: `total_missed_solutions` and `total_extra_problems`. The function should return a dictionary with three keys: `total_time`, `extra_problems`, and `student_time`. 

Assume that the teacher takes one minute to explain each missed solution and give each extra problem, and the student takes one minute to solve each extra problem. Also, assume that the teacher gives one extra problem for every minute the student didn't use.
"""

def calculate_time(total_missed_solutions, total_extra_problems):
    time_per_solution = 1
    time_to_explain_missed_solutions = total_missed_solutions * time_per_solution
    time_per_extra_problem = 1
    time_to_solve_extra_problems = total_extra_problems * time_per_extra_problem
    total_time = time_to_explain_missed_solutions + total_extra_problems
    
    return {
        "total_time": total_time,
        "extra_problems": total_extra_problems,
        "student_time": time_to_solve_extra_problems
    }