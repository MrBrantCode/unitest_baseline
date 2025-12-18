"""
QUESTION:
Adam Ivan is working as a system administrator at Soy Group, Inc. He is now facing at a big trouble: a number of computers under his management have been infected by a computer virus. Unfortunately, anti-virus system in his company failed to detect this virus because it was very new.

Adam has identified the first computer infected by the virus and collected the records of all data packets sent within his network. He is now trying to identify which computers have been infected. A computer is infected when receiving any data packet from any infected computer. The computer is not infected, on the other hand, just by sending data packets to infected computers.

It seems almost impossible for him to list all infected computers by hand, because the size of the packet records is fairly large. So he asked you for help: write a program that can identify infected computers.



Input

The input consists of multiple datasets. Each dataset has the following format:

N M
t1 s1 d1
t2 s2 d2
...
tM sM dM


N is the number of computers; M is the number of data packets; ti (1 ≤ i ≤ M) is the time when the i-th data packet is sent; si and di (1 ≤ i ≤ M) are the source and destination computers of the i-th data packet respectively. The first infected computer is indicated by the number 1; the other computers are indicated by unique numbers between 2 and N.

The input meets the following constraints: 0 < N ≤ 20000, 0 ≤ M ≤ 20000, and 0 ≤ ti ≤ 109 for 1 ≤ i ≤ N; all ti 's are different; and the source and destination of each packet are always different.

The last dataset is followed by a line containing two zeros. This line is not a part of any dataset and should not be processed.

Output

For each dataset, print the number of computers infected by the computer virus.

Example

Input

3 2
1 1 2
2 2 3
3 2
2 3 2
1 2 1
0 0


Output

3
1
"""

def identify_infected_computers(n, m, packets):
    """
    Identifies the number of infected computers based on the given data packets.

    Parameters:
    - n (int): Number of computers.
    - m (int): Number of data packets.
    - packets (list of tuples): List of data packets, where each packet is a tuple (time, source, destination).

    Returns:
    - int: The number of infected computers.
    """
    # Sort packets by time
    packets.sort()
    
    # Initialize the set of infected computers with the first infected computer (computer 1)
    infected = set([1])
    
    # Process each packet
    for (t, s, d) in packets:
        if s in infected:
            infected.add(d)
    
    # Return the number of infected computers
    return len(infected)