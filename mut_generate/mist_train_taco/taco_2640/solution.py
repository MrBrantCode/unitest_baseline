"""
QUESTION:
Mr. Chanek is currently participating in a science fair that is popular in town. He finds an exciting puzzle in the fair and wants to solve it.

There are $N$ atoms numbered from $1$ to $N$. These atoms are especially quirky. Initially, each atom is in normal state. Each atom can be in an excited. Exciting atom $i$ requires $D_i$ energy. When atom $i$ is excited, it will give $A_i$ energy. You can excite any number of atoms (including zero).

These atoms also form a peculiar one-way bond. For each $i$, $(1 \le i < N)$, if atom $i$ is excited, atom $E_i$ will also be excited at no cost. Initially, $E_i$ = $i+1$. Note that atom $N$ cannot form a bond to any atom.

Mr. Chanek must change exactly $K$ bonds. Exactly $K$ times, Mr. Chanek chooses an atom $i$, $(1 \le i < N)$ and changes $E_i$ to a different value other than $i$ and the current $E_i$. Note that an atom's bond can remain unchanged or changed more than once. Help Mr. Chanek determine the maximum energy that he can achieve!

note: You must first change exactly $K$ bonds before you can start exciting atoms.


-----Input-----

The first line contains two integers $N$ $K$ $(4 \le N \le 10^5, 0 \le K < N)$, the number of atoms, and the number of bonds that must be changed.

The second line contains $N$ integers $A_i$ $(1 \le A_i \le 10^6)$, which denotes the energy given by atom $i$ when on excited state.

The third line contains $N$ integers $D_i$ $(1 \le D_i \le 10^6)$, which denotes the energy needed to excite atom $i$.


-----Output-----

A line with an integer that denotes the maximum number of energy that Mr. Chanek can get.


-----Example-----
Input
6 1
5 6 7 8 10 2
3 5 6 7 1 10

Output
35



-----Note-----

An optimal solution to change $E_5$ to 1 and then excite atom 5 with energy 1. It will cause atoms 1, 2, 3, 4, 5 be excited. The total energy gained by Mr. Chanek is (5 + 6 + 7 + 8 + 10) - 1 = 35.

Another possible way is to change $E_3$ to 1 and then exciting atom 3 (which will excite atom 1, 2, 3) and exciting atom 4 (which will excite atom 4, 5, 6). The total energy gained by Mr. Chanek is (5 + 6 + 7 + 8 + 10 + 2) - (6 + 7) = 25 which is not optimal.
"""

def calculate_max_energy(N, K, A, D):
    if K == 0:
        best = 0
        curr = sum(A)
        for i in range(N):
            best = max(best, curr - D[i])
            curr -= A[i]
        return best
    elif K == 1:
        best = sum(A[:-1]) - min(D[:-1])
        other = sum(A)
        other -= sorted(D)[0]
        other -= sorted(D)[1]
        curr = sum(A)
        for i in range(N):
            if i:
                best = max(best, curr - D[i])
            curr -= A[i]
        o2 = sum(A) - min(A[1:]) - D[0]
        return max((best, other, 0, o2))
    else:
        return max((sum(A) - min(D[:-1]), 0, A[-1] - D[-1]))