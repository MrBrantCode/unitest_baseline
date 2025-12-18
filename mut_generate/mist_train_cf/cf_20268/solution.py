"""
QUESTION:
Create a function called `rank_algorithms` that compares and ranks the time and space complexity of three algorithms: Quick Sort, Binary Search Tree, and Bubble Sort. The function should consider the worst-case, average-case, and best-case time complexities, as well as the space complexity for each algorithm. The output should be a ranked list of the algorithms based on their time and space complexities, from best to worst.
"""

def rank_algorithms(algorithms):
    ranked_algorithms = sorted(algorithms, key=lambda x: (x['average_case_time'], x['worst_case_time'], x['space_complexity']))

    return ranked_algorithms

# algorithms with complexities in order from best to worst
algorithms = [
    {'name': 'Quick Sort', 'average_case_time': 'n log n', 'worst_case_time': 'n^2', 'space_complexity': 'log n'},
    {'name': 'Binary Search Tree', 'average_case_time': 'log n', 'worst_case_time': 'n', 'space_complexity': 'n'},
    {'name': 'Bubble Sort', 'average_case_time': 'n^2', 'worst_case_time': 'n^2', 'space_complexity': '1'}
]

ranked_algorithms = rank_algorithms(algorithms)

for i, algorithm in enumerate(ranked_algorithms):
    print(f"{i + 1}. {algorithm['name']}:")
    print(f"   - Best-case time complexity: {algorithm['average_case_time']}")
    print(f"   - Average-case time complexity: {algorithm['average_case_time']}")
    print(f"   - Worst-case time complexity: {algorithm['worst_case_time']}")
    print(f"   - Space complexity: {algorithm['space_complexity']}\n")