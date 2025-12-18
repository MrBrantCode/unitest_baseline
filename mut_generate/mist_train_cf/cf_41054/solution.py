"""
QUESTION:
Write a function `solution(participant, completion)` that takes two lists of participant names as input, where `participant` contains all participants in a race and `completion` contains participants who have completed the race. The function should return the name of the participant who did not complete the race. Assume the `completion` list is one element shorter than the `participant` list. The function must sort both input lists before comparing them.
"""

def findNonCompleter(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]