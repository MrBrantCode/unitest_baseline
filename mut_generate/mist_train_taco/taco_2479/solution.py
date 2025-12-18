"""
QUESTION:
Oleg the client and Igor the analyst are good friends. However, sometimes they argue over little things. Recently, they started a new company, but they are having trouble finding a name for the company.

To settle this problem, they've decided to play a game. The company name will consist of n letters. Oleg and Igor each have a set of n letters (which might contain multiple copies of the same letter, the sets can be different). Initially, the company name is denoted by n question marks. Oleg and Igor takes turns to play the game, Oleg moves first. In each turn, a player can choose one of the letters c in his set and replace any of the question marks with c. Then, a copy of the letter c is removed from his set. The game ends when all the question marks has been replaced by some letter.

For example, suppose Oleg has the set of letters {i, o, i} and Igor has the set of letters {i, m, o}. One possible game is as follows :

Initially, the company name is ???.

Oleg replaces the second question mark with 'i'. The company name becomes ?i?. The set of letters Oleg have now is {i, o}.

Igor replaces the third question mark with 'o'. The company name becomes ?io. The set of letters Igor have now is {i, m}.

Finally, Oleg replaces the first question mark with 'o'. The company name becomes oio. The set of letters Oleg have now is {i}.

In the end, the company name is oio.

Oleg wants the company name to be as lexicographically small as possible while Igor wants the company name to be as lexicographically large as possible. What will be the company name if Oleg and Igor always play optimally?

A string s = s_1s_2...s_{m} is called lexicographically smaller than a string t = t_1t_2...t_{m} (where s ≠ t) if s_{i} < t_{i} where i is the smallest index such that s_{i} ≠ t_{i}. (so s_{j} = t_{j} for all j < i)


-----Input-----

The first line of input contains a string s of length n (1 ≤ n ≤ 3·10^5). All characters of the string are lowercase English letters. This string denotes the set of letters Oleg has initially.

The second line of input contains a string t of length n. All characters of the string are lowercase English letters. This string denotes the set of letters Igor has initially.


-----Output-----

The output should contain a string of n lowercase English letters, denoting the company name if Oleg and Igor plays optimally.


-----Examples-----
Input
tinkoff
zscoder

Output
fzfsirk

Input
xxxxxx
xxxxxx

Output
xxxxxx

Input
ioi
imo

Output
ioi



-----Note-----

One way to play optimally in the first sample is as follows : Initially, the company name is ???????. Oleg replaces the first question mark with 'f'. The company name becomes f??????. Igor replaces the second question mark with 'z'. The company name becomes fz?????. Oleg replaces the third question mark with 'f'. The company name becomes fzf????. Igor replaces the fourth question mark with 's'. The company name becomes fzfs???. Oleg replaces the fifth question mark with 'i'. The company name becomes fzfsi??. Igor replaces the sixth question mark with 'r'. The company name becomes fzfsir?. Oleg replaces the seventh question mark with 'k'. The company name becomes fzfsirk.

For the second sample, no matter how they play, the company name will always be xxxxxx.
"""

def optimal_company_name(oleg_letters: str, igor_letters: str) -> str:
    # Convert input strings to sorted lists
    oleg_sorted = sorted(oleg_letters)
    igor_sorted = sorted(igor_letters, reverse=True)
    
    # Initialize the company name with question marks
    company_name = ['a'] * len(oleg_letters)
    
    # Calculate the lengths for Oleg and Igor's optimal moves
    len1 = len(oleg_letters) // 2 - 1
    len2 = len(oleg_letters) // 2 - 1
    if len(oleg_letters) % 2:
        len1 += 1
    
    # Initialize indices and flags
    i, j = 0, 0
    flag = 0
    ai, aj = 0, 0
    bi, bj = 0, 0
    
    # Fill the company name optimally
    while i + j < len(oleg_letters):
        if i + j < len(oleg_letters):
            if oleg_sorted[ai] < igor_sorted[bi] and flag == 0:
                company_name[i] = oleg_sorted[ai]
                i += 1
                ai += 1
            else:
                company_name[len(oleg_letters) - j - 1] = oleg_sorted[len1 - aj]
                j += 1
                aj += 1
                flag = 1
        
        if i + j < len(oleg_letters):
            if oleg_sorted[ai] < igor_sorted[bi] and flag == 0:
                company_name[i] = igor_sorted[bi]
                i += 1
                bi += 1
            else:
                company_name[len(oleg_letters) - j - 1] = igor_sorted[len2 - bj]
                j += 1
                bj += 1
                flag = 1
    
    # Join the list to form the final company name string
    return ''.join(company_name)