"""
QUESTION:
Write a function `find_all_palindromic_substrings(input_string)` that identifies and returns all unique palindromic substrings from the given input string. The function should have a time complexity of O(n^2), where n is the length of the input string.
"""

def find_all_palindromic_substrings(input_string): 
    n = len(input_string) 
  
    table = [[0 for x in range(n)]for y in range(n)] 
      
    # All substrings of length 1 are by default palindromes
    for i in range(n): 
        table[i][i] = True
  
    # Check all substrings of length 2 
    for cl in range(2, n + 1): 
        for i in range(n - cl + 1): 
            j = i + cl - 1
            if (cl == 2): 
                if (input_string[i] == input_string[j]): 
                    table[i][j] = True
            else: 
                if (input_string[i] == input_string[j] and table[i + 1][j - 1]): 
                    table[i][j] = True
  
    all_pals = []
    for i in range(n):
        for j in range(i, n):
            if table[i][j]:
                all_pals.append(input_string[i : j + 1])
                
    return all_pals