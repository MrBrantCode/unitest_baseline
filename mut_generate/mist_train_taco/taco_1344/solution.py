"""
QUESTION:
Jack has become a soldier now. Unfortunately, he has trouble with the drill. Instead of marching beginning with the left foot and then changing legs with each step, as ordered, he keeps repeating a sequence of steps, in which he sometimes makes the wrong steps or — horror of horrors! — stops for a while. For example, if Jack uses the sequence 'right, left, break', when the sergeant yells: 'Left! Right! Left! Right! Left! Right!', Jack first makes a step with the right foot, then one with the left foot, then he is confused and stops for a moment, then again - this time according to the order - starts with the right foot, then uses the left foot, then - to the sergeant's irritation - he stops to catch his breath, to incorrectly start with the right foot again... Marching this way, Jack will make the step that he is supposed to in the given moment in only one third of cases.

When the officers convinced him he should do something about it, Jack decided to modify the basic sequence of steps that he repeats. However, in order not to get too tired, he has decided that the only thing he'll do is adding any number of breaks in any positions of the original sequence (a break corresponds to stopping for the duration of one step). Of course, Jack can't make a step on the same foot twice in a row, if there is no pause between these steps. It is, however, not impossible that the sequence of steps he used so far is incorrect (it would explain a lot, actually).

Help Private Jack! Given the sequence of steps he keeps repeating, calculate the maximal percentage of time that he can spend marching correctly after adding some breaks to his scheme.

Input

The first line of input contains a sequence consisting only of characters 'L', 'R' and 'X', where 'L' corresponds to a step with the left foot, 'R' — with the right foot, and 'X' — to a break. The length of the sequence will not exceed 106.

Output

Output the maximum percentage of time that Jack can spend marching correctly, rounded down to exactly six digits after the decimal point.

Examples

Input

X


Output

0.000000


Input

LXRR


Output

50.000000

Note

In the second example, if we add two breaks to receive LXXRXR, Jack will march: LXXRXRLXXRXRL... instead of LRLRLRLRLRLRL... and will make the correct step in half the cases. If we didn't add any breaks, the sequence would be incorrect — Jack can't step on his right foot twice in a row.
"""

def calculate_max_correct_marching_percentage(sequence: str) -> float:
    def rate(seq: str) -> int:
        (correct, total, unknown, indicator) = (0, 0, 0, 0)
        left_step = True
        for action in seq:
            if action == 'X':
                total += 1
                left_step = not left_step
            elif (left_step and action == 'L') or (not left_step and action == 'R'):
                correct += 1
                total += 1
                indicator = 0
                left_step = not left_step
            else:
                correct += 1
                total += 2
                unknown += indicator
                indicator = 1 - indicator
        if total % 2 == 1:
            total += 1
            unknown += indicator
        if correct * 2 > total:
            correct -= unknown
            total -= unknown * 2
        return correct * 100000000 // total

    temp = [sequence[0]]
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1] != 'X':
            temp.append('X')
        temp.append(sequence[i])
    augmented = ''.join(temp)
    answer = 0
    if augmented[0] == augmented[-1] != 'X':
        answer = max(rate(augmented + 'X'), rate('X' + augmented))
    else:
        answer = rate(augmented)
    return float(f'{answer / 1000000:.6f}')