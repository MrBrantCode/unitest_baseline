"""
QUESTION:
Write a function `getS(num_coords)` that calculates the aggregate intersection frequency $S(L_n)$ for a given number of coordinates `num_coords`, where the coordinates are generated using the provided formula: $S_0 	=  	290797$, $S_{n+1} 	=  	S_n^2 \bmod 50515093$, and $T_n 	=  	(S_n \bmod 2000) - 1000$. The function should return the value of $S(L_n)$.
"""

from collections import defaultdict

def getS(num_coords):
    S_cur, T = 290797, [0]*2*num_coords
    for i in range(2*num_coords):
        S_cur=(S_cur**2)%50515093
        T[i]=(S_cur%2000)-1000

    Coords = list( zip(T[::2],T[1::2]))
    grads = defaultdict(int)

    for i in range(num_coords):
        for j in range(i):
            deltax, deltay = Coords[i][0] - Coords[j][0], Coords[i][1] - Coords[j][1]

            if deltax==0:
                grad = "inf"
            else:
                grad = deltay/deltax

            grads[grad]+=1

    M = num_coords*(num_coords-1)//2
    num_parallel = sum(n*(n-1)//2 for n in grads.values())

    return M*(M-1)//2 - num_parallel