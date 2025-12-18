"""
QUESTION:
Background

The kindergarten attached to the University of Aizu is a kindergarten where children who love programming gather. Yu, one of the kindergarten children, loves lowercase letters as much as programming. Yu-kun decided to write a scoring program for a new play that uses paper, circles, lines, and lowercase letters.

Problem

Initially, V circles and E lines are drawn on the paper. The circles are numbered from 0 in ascending order, with one lowercase letter or nothing in each circle. Each line connects two different circles. A circle cannot be connected by more than 26 lines.

The play procedure is as follows.

1. Select one circle with nothing written on it. If such a circle does not exist, this process ends.
2. Write one lowercase letter in the circle. However, if the circle is already connected to a circle with lowercase letters by a line, the same lowercase letters as the lowercase letters cannot be written.
3. Return to 1.



After writing lowercase letters in all the circles according to the above procedure, arrange the lowercase letters in the circles in ascending order of the circle numbers to make a character string. I want to minimize the character strings that can be created in this way in lexicographical order. There are two strings s and t of the same length, and s is smaller than t in lexicographical order in the following cases. si represents the i-th lowercase letter of the string s and ti represents the i-th lowercase letter of the string t. For the smallest i where si differs from ti, si is less than ti.

Since the initial state of the paper is given, output the smallest character string that can be created according to the above procedure in lexicographical order.

Constraints

The input satisfies the following conditions.

* 1 ≤ V ≤ 100,000
* 0 ≤ E ≤ 200,000
* ai is either lowercase or'?' (0 ≤ i ≤ V-1)
* 0 ≤ si, ti ≤ V-1 (si <ti, 0 ≤ i ≤ E-1)
* One circle cannot be connected by more than 26 lines

Input


V E
a0 a1 ... a (V-1)
s0 t0
s1 t1
...
s (E-1) t (E-1)


The number of circles V and the number of lines E are given on the first line, separated by blanks.

The initial state of the circle is given on the second line, separated by blanks.

If ai is a lowercase letter, the lowercase letter is written in the i-th circle, and if it is'?', It means that nothing is written in the i-th circle.

The line information is given as si ti on the following E line, which means that the si and ti circles are connected by a line.

Output

Output the smallest character string in the dictionary order on one line among the character strings that can be created according to the procedure in the question sentence.

Examples

Input

3 3
c ? ?
0 1
0 2
1 2


Output

cab


Input

3 2
c ? ?
0 1
0 2


Output

caa


Input

7 6
? a ? ? z a ?
0 1
0 2
3 4
4 5
4 6
5 6


Output

baaazab


Input

5 0
? ? ? ? ?


Output

aaaaa
"""

def generate_minimal_lexicographical_string(V, E, initial_state, edges):
    # Create adjacency list for the graph
    adjacency_list = [[] for _ in range(V)]
    for s, t in edges:
        adjacency_list[s].append(t)
        adjacency_list[t].append(s)
    
    # Process each circle to determine the smallest lexicographical letter
    for i in range(V):
        if 'a' <= initial_state[i] <= 'z':
            continue
        # Set of possible letters (0-25)
        possible_letters = {i for i in range(26)}
        # Remove letters that are already used by connected circles
        for neighbor in adjacency_list[i]:
            if 'a' <= initial_state[neighbor] <= 'z':
                possible_letters.discard(ord(initial_state[neighbor]) - ord('a'))
        # Assign the smallest possible letter to the current circle
        initial_state[i] = chr(min(possible_letters) + ord('a'))
    
    # Join the list to form the final string
    minimal_string = ''.join(initial_state)
    return minimal_string