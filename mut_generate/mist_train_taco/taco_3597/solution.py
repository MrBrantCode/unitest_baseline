"""
QUESTION:
A motorcade of n trucks, driving from city «Z» to city «З», has approached a tunnel, known as Tunnel of Horror. Among truck drivers there were rumours about monster DravDe, who hunts for drivers in that tunnel. Some drivers fear to go first, others - to be the last, but let's consider the general case. Each truck is described with four numbers: 

  * v — value of the truck, of its passangers and cargo 
  * c — amount of passanger on the truck, the driver included 
  * l — total amount of people that should go into the tunnel before this truck, so that the driver can overcome his fear («if the monster appears in front of the motorcade, he'll eat them first») 
  * r — total amount of people that should follow this truck, so that the driver can overcome his fear («if the monster appears behind the motorcade, he'll eat them first»). 



Since the road is narrow, it's impossible to escape DravDe, if he appears from one side. Moreover, the motorcade can't be rearranged. The order of the trucks can't be changed, but it's possible to take any truck out of the motorcade, and leave it near the tunnel for an indefinite period. You, as the head of the motorcade, should remove some of the trucks so, that the rest of the motorcade can move into the tunnel and the total amount of the left trucks' values is maximal. 

Input

The first input line contains integer number n (1 ≤ n ≤ 105) — amount of trucks in the motorcade. The following n lines contain four integers each. Numbers in the i-th line: vi, ci, li, ri (1 ≤ vi ≤ 104, 1 ≤ ci ≤ 105, 0 ≤ li, ri ≤ 105) — describe the i-th truck. The trucks are numbered from 1, counting from the front of the motorcade.

Output

In the first line output number k — amount of trucks that will drive into the tunnel. In the second line output k numbers — indexes of these trucks in ascending order. Don't forget please that you are not allowed to change the order of trucks. If the answer is not unique, output any.

Examples

Input

5
1 1 0 3
1 1 1 2
1 1 2 1
1 1 3 0
2 1 3 0


Output

4
1 2 3 5 


Input

5
1 1 0 3
10 1 2 1
2 2 1 1
10 1 1 2
3 1 3 0


Output

3
1 3 5
"""

def maximize_truck_values(n, trucks):
    v = [truck[0] for truck in trucks]
    c = [truck[1] for truck in trucks]
    L = [truck[2] for truck in trucks]
    R = [truck[3] for truck in trucks]
    
    index = [i for i in range(n)]
    index.sort(key=lambda i: (c[i] + L[i] + R[i], i))
    
    prev = n * [-1]
    best_res = 0
    best_last = -1
    ii = 0
    
    while ii < n:
        i = index[ii]
        jj = ii
        d = {0: (0, -1)}
        
        while jj < n:
            j = index[jj]
            if c[i] + L[i] + R[i] != c[j] + L[j] + R[j]:
                break
            x = d.get(L[j])
            if x is not None:
                cur = v[j] + x[0]
                prev[j] = x[1]
                if R[j] == 0 and cur > best_res:
                    best_res = cur
                    best_last = j
                y = d.get(L[j] + c[j])
                if y is None or cur > y[0]:
                    d[L[j] + c[j]] = (cur, j)
            jj += 1
        ii = jj
    
    ans = []
    while best_last != -1:
        ans.append(best_last)
        best_last = prev[best_last]
    
    ans.reverse()
    for i in range(len(ans)):
        ans[i] += 1
    
    k = len(ans)
    return k, ans