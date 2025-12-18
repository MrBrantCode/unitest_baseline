"""
QUESTION:
Some scientists are working on protein recombination, and during their research, they have found a remarkable fact: there are 4 proteins in the protein ring that mutate after every second according to a fixed pattern. For simplicity, proteins are called $A,B,C,D$ (you know, protein names can be very complicated). A protein mutates into another one depending on itself and the protein right after it. Scientists determined that the mutation table goes like this:  

    A   B   C   D
    _   _   _   _
A|  A   B   C   D
B|  B   A   D   C
C|  C   D   A   B
D|  D   C   B   A

Here rows denote the protein at current position, while columns denote the protein at the next position. And the corresponding value in the table denotes the new protein that will emerge. So for example, if protein i is A, and protein i + 1 is B, protein i will change to B. All mutations take place simultaneously. The protein ring is seen as a circular list, so last protein of the list mutates depending on the first protein. 

Using this data, they have written a small simulation software to get mutations second by second. The problem is that the protein rings can be very long (up to 1 million proteins in a single ring) and they want to know the state of the ring after upto $\mathbf{10^{9}}$ seconds. Thus their software takes too long to report the  results. They ask you for your help.  

Input Format

Input contains 2 lines. 

First line has 2 integers $N$ and $\mbox{K}$, $N$ being the length of the protein ring and $\mbox{K}$ the desired number of seconds. 

Second line contains a string of length $N$ containing uppercase letters $\mbox{A}$,$\mbox{B}$, $\mbox{C}$ or $\mbox{D}$ only, describing the ring. 

Constraints

$1\leq N\leq10^6$ 

$1\leq K\leq10^9$ 

Output Format

Output a single line with a string of length $N$, describing the state of the ring after $\mbox{K}$ seconds.

Sample Input 0
5 15
AAAAD

Sample Output 0
DDDDA

Explanation 0

The complete sequence of mutations is:

AAADD
AADAD
ADDDD
DAAAD
DAADA
DADDD
DDAAA
ADAAD
DDADD
ADDAA
DADAA
DDDAD
AADDA
ADADA
DDDDA
"""

def simulate_protein_ring_mutation(N, K, initial_state):
    c2i = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    i2c = ['A', 'B', 'C', 'D']
    
    # Convert initial state to integer list
    s = [c2i[x] for x in initial_state]
    s = [s, [0] * N]
    
    (a, b) = (1, 0)
    
    while K > 0:
        a, b = b, a
        cp2 = 1
        for i in range(29, 0, -1):
            if K - (1 << i) >= 0:
                cp2 = 1 << i
                break
        K -= cp2
        for i in range(N):
            s[b][i] = s[a][i] ^ s[a][(i + cp2) % N]
    
    # Convert result back to character list
    result = ''.join(i2c[i] for i in s[b])
    return result