"""
QUESTION:
Given a dictionary of words and an M x N board where every cell has one character. Find all possible different words from the dictionary that can be formed by a sequence of adjacent characters on the board. We can move to any of 8 adjacent characters, but a word should not have multiple instances of the same cell.
Example 1:
Input: 
N = 1
dictionary = {"CAT"}
R = 3, C = 3
board = {{C,A,P},{A,N,D},{T,I,E}}
Output:
CAT
Explanation: 
C A P
A N D
T I E
Words we got is denoted using same color.
Example 2:
Input:
N = 4
dictionary = {"GEEKS","FOR","QUIZ","GO"}
R = 3, C = 3 
board = {{G,I,Z},{U,E,K},{Q,S,E}}
Output:
GEEKS QUIZ
Explanation: 
G I Z
U E K
Q S E 
Words we got is denoted using same color.
Your task:
You don’t need to read input or print anything. Your task is to complete the function wordBoggle() which takes the dictionary contaning N space-separated strings and R*C board as input parameters and returns a list of words that exist on the board (NOTE: All words returned must be different even it occurs multiple times in the dictionary).
Expected Time Complexity: O(4^(N^2))
Expected Auxiliary Space: O(N^2)
Constraints:
1 ≤ N ≤ 15
1 ≤ R, C ≤ 50
1 ≤ length of Word ≤ 60
All words of Dictionary and all characters of board are in uppercase letters from 'A' to 'Z'
"""

def find_words_on_board(board, dictionary):
    def dfs(r, c, pos, word):
        if pos == len(word):
            return True
        if 0 <= r < len(board) and 0 <= c < len(board[0]) and not visited[r][c] and board[r][c] == word[pos]:
            visited[r][c] = True
            if (dfs(r + 1, c, pos + 1, word) or
                dfs(r, c + 1, pos + 1, word) or
                dfs(r - 1, c, pos + 1, word) or
                dfs(r, c - 1, pos + 1, word) or
                dfs(r + 1, c + 1, pos + 1, word) or
                dfs(r + 1, c - 1, pos + 1, word) or
                dfs(r - 1, c + 1, pos + 1, word) or
                dfs(r - 1, c - 1, pos + 1, word)):
                return True
            visited[r][c] = False
        return False

    found_words = []
    for word in dictionary:
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, word):
                        found_words.append(word)
                        break
            else:
                continue
            break

    return list(set(found_words))