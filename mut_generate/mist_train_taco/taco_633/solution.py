"""
QUESTION:
Do you know Just Odd Inventions? The business of this company is to "just odd inventions". Here, it is abbreviated as JOI.

JOI is conducting research to confine many microorganisms in one petri dish alive. There are N microorganisms to be investigated, and they are numbered 1, 2, ..., N. When each microorganism is trapped in a petri dish, it instantly releases a harmful substance called foo (fatally odd object) into the petri dish. The amount of foo released by each microorganism is known. The foo released by all the microorganisms trapped in the petri dish is evenly ingested by each microorganism in the petri dish. The foo tolerance of each microorganism is known, and if foo is ingested in excess of this amount, the microorganism will die.

The foo release amount of the microorganism i is ai milligrams, and the foo tolerance is bi milligrams. That is, when the microorganisms i1, i2, ..., ik are trapped in the petri dish, each microorganism in the petri dish ingests (ai1 + ai2 + ... + aik) / k milligrams of foo, and the microorganisms in the petri dish ingest. i will die if this intake is greater than bi.

On behalf of JOI, you must keep as many microorganisms alive in the petri dish as possible. However, no microbes in the petri dish should die from ingestion of foo, as carcasses of microorganisms adversely affect the environment in the petri dish.

It is still a mystery how JOI profits from making "just a strange invention", and no one in JOI knows except the president.



input

Read the following input from standard input.

* The integer N is written on the first line, which indicates that there are N microorganisms to be investigated.
* The following N lines contain information on each microorganism. On the first line of i + (1 ≤ i ≤ N), the positive integers ai and bi are written separated by blanks, and the foo emission amount of the microorganism i is ai milligrams and the foo tolerance is bi milligrams. Represent.

output

Output the maximum number of microorganisms that can be confined in one petri dish to the standard output in one line.

Example

Input

6
12 8
5 9
2 4
10 12
6 7
13 9


Output

3
"""

import heapq

def max_surviving_microorganisms(N, microorganisms):
    # Sort microorganisms by their foo emission amount (ai)
    microorganisms.sort()
    
    Q = []
    ans = s = sz = 0
    
    for t in microorganisms:
        s += t[0]
        heapq.heappush(Q, (t[1], t[0]))
        sz += 1
        
        while sz and sz * Q[0][0] < s:
            s -= Q[0][1]
            heapq.heappop(Q)
            sz -= 1
        
        if sz > ans:
            ans = sz
    
    return ans