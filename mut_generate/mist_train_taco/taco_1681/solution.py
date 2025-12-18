"""
QUESTION:
Nathan O. Davis is trying to capture a game and struggling to get a very rare item. This rare item can be obtained by arranging special patterns in a row on a casino slot machine. The slot machine has N reels, and pressing the button once stops the currently rotating leftmost reel. Therefore, you need to press the button N times to get this rare item. Also, in order to stop with a special pattern, it is necessary to press the button at a certain timing. However, the timing of pressing this button was very severe, so I was in trouble because it didn't go well. Therefore, Nathan decided to analyze the game while checking the memory value during the game using the memory viewer.

As a result of Nathan's analysis, in order to stop the reel with that special pattern, the "random number" written at address 007E0D1F in the memory must have a specific value when the button is pressed. I found out. It was also found that the value of the random number changes every frame by the linear congruential method, and whether or not the button is pressed is judged once every frame. Here, the linear congruential method is one of the methods for generating pseudo-random numbers, and the value is determined by the following formula.

x'= (A x x + B) mod C

Here, x is the value of the current random number, x'is the value of the next random number, and A, B, and C are some constants. Also, y mod z represents the remainder when y is divided by z.

For example, suppose a slot machine with two reels has A = 5, B = 7, C = 11 and the first "random number" value is 10. And, the condition for stopping the reel with a special pattern is that the reel on the left side is 2 and the reel on the right side is 4. At this time, the value of the random number in the first frame is (5 × 10 + 7) mod 11 = 2, so if you press the button in the first frame, the reel on the left side will stop with a special pattern. Since the value of the random number in the second frame that follows is (5 x 2 + 7) mod 11 = 6, the reel on the right side does not stop with a special pattern even if the button is pressed in the second frame. In the following 3rd frame, the random number value becomes (5 x 6 + 7) mod 11 = 4, so if you press the button in the 3rd frame, the reel on the right side will stop with a special pattern. Therefore, all reels can be stopped with a special pattern in a minimum of 3 frames, and rare items can be obtained.

Your job is to help Nathan get a rare item by writing a program that asks how many frames in the shortest frame all reels can be stopped with a special pattern. ..

Input

The input consists of multiple datasets. Each dataset is given in the following format.

> N A B C X
> Y1 Y2 ... YN

The first row contains five integers N (1 ≤ N ≤ 100), A, B (0 ≤ A, B ≤ 10,000), C (1 ≤ C ≤ 10,000), and X (0 ≤ X <C), respectively. It is given separated by two whitespace characters. Here, X represents the value of the first random number. On the following line, N integers Y1, Y2, ..., YN (0 ≤ Yi ≤ 10,000) are given, separated by a single space character. These represent the conditions for stopping the reel with a specific pattern, and the i-th number Yi is the random number value Yi to stop the i-th reel from the left with a special pattern. It means that there must be.

The end of the input is indicated by a single line containing five zeros separated by blanks.

Output

For each dataset, output the shortest number of frames required to stop at a special pattern on one line. If it cannot be stopped within 10,000 frames, output -1 instead of the number of frames. The output must not contain extra blanks or line breaks.

Sample Input


1 5 7 11 10
Ten
2 5 7 11 10
twenty four
2 1 1 256 0
128 255
2 0 0 1 0
1 2 3 4 5 6 7 8
2 1 1 100 0
99 98
2 1 1 100 0
99 99
2 1 1 10000 0
Ten
2 1 1 10000 0
twenty one
0 0 0 0 0


Output for the Sample Input


0
3
255
-1
198
199
10000
-1






Example

Input

1 5 7 11 10
10
2 5 7 11 10
2 4
2 1 1 256 0
128 255
2 0 0 1 0
1234 5678
2 1 1 100 0
99 98
2 1 1 100 0
99 99
2 1 1 10000 0
1 0
2 1 1 10000 0
2 1
0 0 0 0 0


Output

0
3
255
-1
198
199
10000
-1
"""

def find_minimum_frames(N, A, B, C, X, Y):
    def calc(A, B, C, X):
        return (A * X + B) % C
    
    frame_count = 0
    
    while frame_count <= 10000:
        if X == Y[0]:
            Y.pop(0)
            if not Y:
                return frame_count
        X = calc(A, B, C, X)
        frame_count += 1
    
    return -1