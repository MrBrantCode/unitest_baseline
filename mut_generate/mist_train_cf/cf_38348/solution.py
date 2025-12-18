"""
QUESTION:
Implement the `execute_tasks_concurrently` function to process a list of JSON objects concurrently using the `concurrent.futures` module. Each JSON object represents a task with a "function" field specifying the function to be executed and an "args" field specifying the arguments to be passed to the function. The function should define and execute the following functions: `square` (accepts one argument and returns its square), `cube` (accepts one argument and returns its cube), and `sum_of_squares` (accepts two arguments and returns the sum of their squares). The function should return the results of each task execution in the order they were processed. The input list of JSON objects and the results of task execution should be as follows:

Input: `[{"function": "square", "args": [2]}, {"function": "cube", "args": [3]}, {"function": "sum_of_squares", "args": [4, 5]}]`
Output: `[4, 27, 41]`

Note: Use the `concurrent.futures` module to process the tasks concurrently.
"""

import concurrent.futures as cf

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def sum_of_squares(x, y):
    return x ** 2 + y ** 2

def execute_tasks_concurrently(tasks):
    def execute_task(task):
        function_name = task["function"]
        args = task["args"]
        if function_name == "square":
            result = square(*args)
        elif function_name == "cube":
            result = cube(*args)
        elif function_name == "sum_of_squares":
            result = sum_of_squares(*args)
        return result

    with cf.ThreadPoolExecutor() as executor:
        results = list(executor.map(execute_task, tasks))

    return results