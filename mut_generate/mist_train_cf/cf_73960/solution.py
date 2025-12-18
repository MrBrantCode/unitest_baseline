"""
QUESTION:
Write a function `min_salary(salary_demands)` that calculates the minimum cost to hire an employee over a certain period given a list of daily salary demands, where an employee must be hired for at least one day before they can be fired. The function should return the minimum total cost for the given period.
"""

def min_salary(salary_demands):
    n = len(salary_demands)
    min_costs = [0]*n
    min_costs[0] = salary_demands[0]
    for i in range(1,n):
        min_costs[i] = min(min_costs[i-1], salary_demands[i])
    return sum(min_costs)