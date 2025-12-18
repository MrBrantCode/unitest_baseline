"""
QUESTION:
I decided to do bowling as a recreation of the class. Create a program that inputs the pitching information for each participant and outputs the grade information in descending order of score. If there is a tie, output in ascending order of student ID number. However, it is assumed that the number of participants is 3 or more and 40 or less, and one game is thrown per person.

Bowling is a sport in which the player rolls the ball toward 10 pins arranged in an equilateral triangle with the vertices facing the player and knocks down the pins. The case where all the players fall in the first pitch is called a strike, and only that pitch advances to the next frame. If it is not a strike, leave the remaining pins and make a second pitch. A spare is when all the pitches have fallen on the second pitch. After the second pitch, proceed to the next frame.

One game consists of 10 frames, and each of the 1st to 9th frames can be pitched twice. At the beginning of each frame, all 10 pins are upright. In the 10th frame, if there is a strike or a spare, a total of 3 pitches will be thrown, otherwise 2 pitches will be made and the game will end.

Score example 1
<image>

Score example 2 (when the maximum score is 300 points)
<image>



How to calculate the score

* If there are no spares or strikes in each frame, the number of pins defeated in two pitches will be the score for that frame. (4th and 8th frames of score example 1)
* If you give a spare, in addition to the number of defeated 10 points, the number of defeated pins in the next pitch will be added to the score of this frame. (Relationship between the 1st frame and the 2nd frame of the score example 1) In the 1st frame of the score example 1, 20 points including 10 points (points) defeated by 1 throw of the 2nd frame will be scored. The calculation method is the same for the third frame.
* If you strike, the number of pins you defeated in the next two pitches will be added to the number of defeated 10 points. (Relationship between the 2nd frame and the 3rd frame of score example 1) Of course, there may be a strike during the following 2 throws. (Relationship between the 5th frame and the 6th and 7th frames of score example 1)
* If you give a spare or strike only in the 10th frame, the total number of pins you have thrown and defeated will be added as the score in the 10th frame.
* The total score of each frame is the score of one game, and the maximum score is 300 points.



Input

A sequence of multiple datasets is given as input. The end of the input is indicated by a single line of zeros. Each dataset is given in the following format:


m
score1
score2
::
scorem


The number of participants m (3 ≤ m ≤ 40) is given in the first line, and the i-th participant information scorei is given in the following m lines. Each participant information is given in the following format, one line at a time.


id s1 s2 ... sn


The student ID number id (0 ≤ id ≤ 9999) is given first, followed by the number of fall pins of the jth throw sj (0 ≤ sj ≤ 10). It is assumed that the total number of pitches n is 12 or more and 21 or less, and the number of pins required for score calculation is given in just proportion.

Output

For each input dataset, the student ID number and score are output in descending order of score (if there is a tie, the student ID number is in ascending order). Please separate your student ID number and score with one space and output them on one line.

Example

Input

3
1010 6 3 10 7 1 0 7 9 1 10 6 2 4 3 9 1 9 0
1200 5 3 9 1 7 1 0 0 8 1 10 10 4 3 9 1 8 2 9
1101 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
4
3321 8 2 10 9 1 7 0 10 10 10 0 8 10 10 10 10
3332 5 0 10 9 1 4 1 9 0 10 10 7 1 5 2 8 1
3335 10 10 10 10 10 10 10 10 10 10 10 10
3340 8 2 7 3 6 4 8 2 8 2 9 1 7 3 6 4 8 2 9 1 7
0


Output

1200 127
1010 123
1101 60
3335 300
3321 200
3340 175
3332 122
"""

def calculate_bowling_scores(participants):
    def calculate_score(scores):
        score = 0
        frame = 1
        index = 0
        while frame <= 10:
            if scores[index] == 10:  # Strike
                score += 10 + scores[index + 1] + scores[index + 2]
                index += 1
            else:
                if scores[index] + scores[index + 1] == 10:  # Spare
                    score += 10 + scores[index + 2]
                else:
                    score += scores[index] + scores[index + 1]
                index += 2
            frame += 1
        return score

    results = []
    for participant in participants:
        student_id, scores = participant
        total_score = calculate_score(scores)
        results.append((student_id, total_score))
    
    results.sort(key=lambda x: x[0])  # Sort by student ID first
    results.sort(key=lambda x: x[1], reverse=True)  # Then sort by score in descending order
    
    return results