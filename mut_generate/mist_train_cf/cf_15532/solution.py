"""
QUESTION:
Create a function called `calculate_levenshtein_distance` that takes in two strings `str1` and `str2` as input. The function should return the minimum number of operations (insertions, deletions, or substitutions) required to transform `str1` into `str2`. Additionally, print out the minimum number of operations required for each step of the transformation process. The function should handle cases where the strings are of different lengths and contain duplicate characters.
"""

def calculate_levenshtein_distance(str1, str2):
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    
    for i in range(len(str1) + 1):
        dp[i][0] = i
        
    for j in range(len(str2) + 1):
        dp[0][j] = j
        
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    
    min_operations = dp[len(str1)][len(str2)]
    print("Minimum operations required:", min_operations)
    
    i, j = len(str1), len(str2)
    steps = []
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and str1[i - 1] == str2[j - 1]:
            i -= 1
            j -= 1
        elif j > 0 and (i == 0 or dp[i][j - 1] <= dp[i - 1][j] and dp[i][j - 1] <= dp[i - 1][j - 1]):
            steps.append(f"Step {min_operations - dp[i][j]}: {str1[:i]} -> {str1[:i] + str2[j - 1]} (insert '{str2[j - 1]}' at position {i})")
            j -= 1
        elif i > 0 and (j == 0 or dp[i - 1][j] <= dp[i][j - 1] and dp[i - 1][j] <= dp[i - 1][j - 1]):
            steps.append(f"Step {min_operations - dp[i][j]}: {str1[:i - 1]}{str1[i:]} -> {str1[:i - 1]}{str2[j]} (delete '{str1[i - 1]}' at position {i - 1})")
            i -= 1
        else:
            steps.append(f"Step {min_operations - dp[i][j]}: {str1[:i - 1]}{str1[i:]} -> {str1[:i - 1]}{str2[j - 1]} (substitute '{str2[j - 1]}' for '{str1[i - 1]}' at position {i - 1})")
            i -= 1
            j -= 1
    
    for step in reversed(steps):
        print(step)
    
    return min_operations