"""
QUESTION:
An angel lives in the clouds above the city where Natsume lives. The angel, like Natsume, loves cats and often comes down to the ground to play with cats. To get down to the ground, the angel made a long, long staircase leading from the clouds to the ground. However, the angel thought that it would be boring to just go down every time, so he worked on the stairs so that he could make a sound when he stepped on the steps. Use this to get off while playing music.

Music is played using 12 kinds of sounds. This time, I will ignore the octave of the sound and consider only 12 types of C, C #, D, D #, E, F, F #, G, G #, A, A #, B. The difference between adjacent sounds is called a semitone. For example, raising C by a semitone gives C #, and raising C # by a semitone gives D. Conversely, lowering G by a semitone gives F #, and lowering F # by a semitone gives F. Note that raising E by a semitone results in F, and raising B by a semitone results in C.

The mechanism of sound output from the stairs is as follows. First, the stairs consist of n white boards floating in the air. One of the 12 tones is assigned to each of the 1st to nth boards counting from the clouds. Let's write this as Ti (i = 1 ... n). Also, for the sake of simplicity, consider the clouds as the 0th stage and the ground as the n + 1th stage (however, no scale is assigned to them). When the angel is in the k (k = 0 ... n) stage, the next step is to go to any of the k-1, k + 1, k + 2 stages that exist. However, it cannot move after descending to the n + 1th stage (ground), and cannot return to it after leaving the 0th stage (cloud). Each movement makes a sound according to the following rules.

I got down to the k + 1 stage
The sound of Tk + 1 sounds.
k + 2nd step
A semitone up of Tk + 2 sounds.
I returned to the k-1 stage
A semitone lower Tk-1 sounds.

Information on the stairs T1 ... Tn and the song S1 ... Sm that the angel wants to play are given. At this time, another sound must not be played before, during, or after the song you want to play. Determine if the angel can play this song and descend from the clouds to the ground.

Notes on Submission

Multiple datasets are given in the above format. The first line of input data gives the number of datasets. Create a program that outputs the output for each data set in order in the above format.



Input

The first line of input gives the number of steps n of the stairs and the length m of the song that the angel wants to play. The second line is the information of the stairs, and T1, T2, ..., Tn are given in this order. The third line is the song that the angel wants to play, and S1, S2, ..., Sm are given in this order. All of these are separated by a single space character and satisfy 1 <= n, m <= 50000.

Output

Output "Yes" if the angel can get down to the ground while playing the given song, otherwise output "No" on one line.

Example

Input

4
6 4
C E D# F G A
C E F G
6 4
C E D# F G A
C D# F G
3 6
C D D
D# B D B D# C#
8 8
C B B B B B F F
C B B B B B B B


Output

Yes
No
Yes
No
"""

def can_angel_play_song(n, m, t_lst, s_lst):
    # Dictionary to map tones to their semitone indices
    dic = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}
    
    # Convert the staircase tones and song tones to their semitone indices
    t_lst = [-100] + [dic[tone] for tone in t_lst]
    s_lst = [dic[tone] for tone in s_lst]
    s_lst.reverse()

    def search(stack):
        (t_index, s_index) = stack.pop()
        if s_index == m:
            return t_index == 0
        if t_index <= 0 or t_index > n:
            return False
        base = t_lst[t_index]
        proc = s_lst[s_index]
        diff = (proc - base) % 12
        if diff == 1:
            stack.append((t_index - 2, s_index + 1))
        if diff == 0:
            stack.append((t_index - 1, s_index + 1))
        if diff == 11:
            stack.append((t_index + 1, s_index + 1))
        return False

    stack = [(n, 0), (n - 1, 0)]
    while stack:
        if search(stack):
            return True
    return False