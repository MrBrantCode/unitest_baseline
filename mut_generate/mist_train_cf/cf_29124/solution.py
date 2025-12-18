"""
QUESTION:
Implement the function `top_contributors(commit_history, k)` that takes a list of strings representing the commit history of a repository and a positive integer `k` as input, and returns a list of the names of the top `k` most active contributors in descending order of their activity. The function should handle cases where there are fewer than `k` contributors.
"""

def top_contributors(commit_history, k):
    contributor_counts = {}
    for contributor in commit_history:
        if contributor in contributor_counts:
            contributor_counts[contributor] += 1
        else:
            contributor_counts[contributor] = 1

    sorted_contributors = sorted(contributor_counts.items(), key=lambda x: x[1], reverse=True)
    return [contributor[0] for contributor in sorted_contributors[:k]]