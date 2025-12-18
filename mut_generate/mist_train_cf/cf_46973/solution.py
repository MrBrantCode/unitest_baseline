"""
QUESTION:
Implement the function `peopleIndices(favoriteCompanies, char)` that takes a 2D list `favoriteCompanies` and a character `char` as input, and returns a list of indices of people whose list of favorite companies is not a subset of any other list of favorites companies and contains the character `char`. The function should return the indices in increasing order. The input constraints are:
- `1 <= favoriteCompanies.length <= 100`
- `1 <= favoriteCompanies[i].length <= 500`
- `1 <= favoriteCompanies[i][j].length <= 20`
- All strings in `favoriteCompanies[i]` are distinct and consist of lowercase English letters only.
- The character `char` is a lowercase English letter.
"""

def peopleIndices(favoriteCompanies, char):
    n = len(favoriteCompanies)
    favSets = [set(fav) for fav in favoriteCompanies]
    result = []
    for i in range(n):
        if any(favSets[i] < favSets[j] for j in range(n) if j != i):
            continue
        if any(char in company for company in favoriteCompanies[i]):
            result.append(i)
    return result