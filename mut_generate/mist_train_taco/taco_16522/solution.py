"""
QUESTION:
Hansa loves dancing and so do her friends. But she has some pretty weird friends. Like this one friend of hers, Jack, jumps forward while dancing. The dance floor is of finite length (L) and there are many people dancing on it. During each song, Jack jumps exactly X steps forward and at the end of the song, he is pushed back Y steps by the other dancers. 

Every class has a nerd. This one does too. The nerd doesn’t like dancing but in order to kill time he is watching this jumping Jack. He is counting the number of songs that have been played before Jack reaches the end of the dance floor. Tell us how many songs he counted.

Note: Even if a song doesn’t complete when he reaches the end of the dance floor, but it has started, then it is counted.

Input:
Three space separated integers L, X, Y.

Output:
A single line of output that is the answer to the question.

Constraints:
1 ≤ Y < X ≤ L ≤ 10^9

Problem Setter: Chintan Shah

SAMPLE INPUT
6 5 1

SAMPLE OUTPUT
2
"""

def count_songs_to_reach_end(L, X, Y):
    # Initialize the count of songs
    c = 0
    # Initialize the current position of Jack
    current_position = 0
    
    # Loop until Jack reaches or exceeds the end of the dance floor
    while current_position < L:
        # Increment the count of songs
        c += 1
        # Jack jumps forward
        current_position += X
        # Check if Jack has reached or exceeded the end of the dance floor
        if current_position >= L:
            break
        # Jack is pushed back
        current_position -= Y
    
    return c