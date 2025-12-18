"""
QUESTION:
There are 3^N people dancing in circle. We denote with 0,1,\dots, 3^{N}-1 the positions in the circle, starting from an arbitrary position and going around clockwise. Initially each position in the circle is occupied by one person.

The people are going to dance on two kinds of songs: salsa and rumba.

* When a salsa is played, the person in position i goes to position j, where j is the number obtained replacing all digits 1 with 2 and all digits 2 with 1 when reading i in base 3 (e.g., the person in position 46 goes to position 65).
* When a rumba is played, the person in position i moves to position i+1 (with the identification 3^N = 0).



You are given a string T=T_1T_2\cdots T_{|T|} such that T_i=`S` if the i-th song is a salsa and T_i=`R` if it is a rumba. After all the songs have been played, the person that initially was in position i is in position P_i. Compute the array P_0,P_1,\dots, P_{3^N-1}.

Constraints

* 1 \le N \le 12
* 1 \le |T| \le 200,000
* T contains only the characters `S` and `R`.

Input

Input is given from Standard Input in the following format:


N
T


Output

You should print on Standard Output:


P_0 P_1 \cdots P_{3^N-1}

Output

You should print on Standard Output:


P_0 P_1 \cdots P_{3^N-1}

Examples

Input

1
SRS


Output

2 0 1


Input

2
RRSRSSSSR


Output

3 8 1 0 5 7 6 2 4


Input

3
SRSRRSRRRSRRRR


Output

23 9 22 8 3 7 20 24 19 5 18 4 17 12 16 2 6 1 14 0 13 26 21 25 11 15 10
"""

def compute_final_positions(n: int, t: str) -> list[int]:
    new_pos = [0]
    new_w = [0] * len(t)
    
    for i in range(1, n + 1):
        ith_bit = [0] * 3 ** i
        for k in range(3):
            for l in range(3 ** (i - 1)):
                ith_bit[k * 3 ** (i - 1) + l] = k
        
        pos = new_pos
        w = new_w
        q = 0
        already = [0] * 3 ** i
        new_w = [0] * len(t)
        
        for j in range(len(t)):
            mark = w[j]
            for k in range(3):
                cand = mark + k * 3 ** (i - 1)
                if ith_bit[cand] and (q - already[cand]) % 2:
                    ith_bit[cand] = 3 - ith_bit[cand]
                already[cand] = q
                if ith_bit[cand] == 2:
                    new_w[j] = cand
            
            if t[j] == 'S':
                q += 1
            else:
                for k in range(3):
                    ith_bit[mark + k * 3 ** (i - 1)] = (ith_bit[mark + k * 3 ** (i - 1)] + 1) % 3
        
        new_pos = [0] * 3 ** i
        for j in range(3 ** i):
            if ith_bit[j] and (q - already[j]) % 2:
                ith_bit[j] = 3 - ith_bit[j]
            new_pos[j] = pos[j % 3 ** (i - 1)] + ith_bit[j] * 3 ** (i - 1)
    
    return new_pos