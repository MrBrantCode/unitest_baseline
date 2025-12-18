"""
QUESTION:
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications: 

Mat size must be $N$X$\mbox{M}$. ($N$ is an odd natural number, and $\mbox{M}$ is $3$ times $N$.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------

Input Format

A single line containing the space separated values of $N$ and $\mbox{M}$.  

Constraints

$5<N<101$
$15<M<303$

Output Format

Output the design pattern.

Sample Input
9 27

Sample Output
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""

def generate_door_mat(N, M):
    # Initialize the list to hold the lines of the door mat
    mat = []
    
    # Generate the top part of the door mat
    for i in range(1, N, 2):
        pattern = '.|.' * i
        padding = '-' * ((M - len(pattern)) // 2)
        mat.append(padding + pattern + padding)
    
    # Generate the middle part with 'WELCOME'
    welcome_padding = '-' * ((M - len('WELCOME')) // 2)
    mat.append(welcome_padding + 'WELCOME' + welcome_padding)
    
    # Generate the bottom part of the door mat
    for i in range(N - 2, -1, -2):
        pattern = '.|.' * i
        padding = '-' * ((M - len(pattern)) // 2)
        mat.append(padding + pattern + padding)
    
    return mat