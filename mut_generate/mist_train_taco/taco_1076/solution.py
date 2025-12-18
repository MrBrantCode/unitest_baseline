"""
QUESTION:
Chef recently saw the movie Matrix. He loved the movie overall but he didn't agree with some things in it. Particularly he didn't agree with the bald boy when he declared - There is no spoon. Being a chef, he understands the importance of the spoon and realizes that the universe can't survive without it. Furthermore, he is sure there is a spoon; he saw it in his kitchen this morning. So he has set out to prove the bald boy is wrong and find a spoon in the matrix. He has even obtained a digital map already. Can you help him?

Formally you're given a matrix of lowercase and uppercase Latin letters. Your job is to find out if the word "Spoon" occurs somewhere in the matrix or not. A word is said to be occurred in the matrix if it is presented in some row from left to right or in some column from top to bottom. Note that match performed has to be case insensitive. 

------ Input ------ 

The first line of input contains a positive integer T, the number of test cases. After that T test cases follow. The first line of each test case contains two space separated integers R and C, the number of rows and the number of columns of the matrix M respectively. Thereafter R lines follow each containing C characters, the actual digital map itself.

------ Output ------ 

For each test case print one line. If a "Spoon" is found in Matrix, output "There is a spoon!" else output "There is indeed no spoon!" (Quotes only for clarity).

------ Constraints ------ 

1 ≤ T ≤ 100

1 ≤ R, C ≤ 100

----- Sample Input 1 ------ 
3
3 6
abDefb
bSpoon
NIKHil
6 6
aaaaaa
ssssss
xuisdP
oooooo
ioowoo
bdylan
6 5
bdfhj
cacac
opqrs
ddddd
india
yucky
----- Sample Output 1 ------ 
There is a spoon!
There is a spoon!
There is indeed no spoon!
----- explanation 1 ------ 
In the first test case, "Spoon" occurs in the second row. In the second test case, "spOon" occurs in the last column.
"""

def find_spoon_in_matrix(test_cases):
    results = []
    
    for case in test_cases:
        R, C, matrix = case
        matrix = [row.lower() for row in matrix]
        found = False
        
        # Check rows for "spoon"
        for row in matrix:
            if 'spoon' in row:
                found = True
                break
        
        # If not found in rows, check columns for "spoon"
        if not found:
            for col in range(C):
                for row in range(R - 4):
                    if (matrix[row][col] == 's' and
                        matrix[row + 1][col] == 'p' and
                        matrix[row + 2][col] == 'o' and
                        matrix[row + 3][col] == 'o' and
                        matrix[row + 4][col] == 'n'):
                        found = True
                        break
                if found:
                    break
        
        if found:
            results.append("There is a spoon!")
        else:
            results.append("There is indeed no spoon!")
    
    return results