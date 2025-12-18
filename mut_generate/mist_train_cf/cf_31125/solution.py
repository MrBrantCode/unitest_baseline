"""
QUESTION:
Write a function `max_thieves_captured` that takes two parameters: `distancia`, an integer representing the maximum distance within which a police officer can catch a thief, and `individuos`, a list of characters representing individuals in a line, where 'P' denotes a police officer and 'L' denotes a thief. The function should return the maximum number of thieves that can be caught by the police officers.
"""

def max_thieves_captured(distancia, individuos):
    max_thieves = 0
    n = len(individuos)
    for i in range(n):
        if individuos[i] == 'P':
            start = max(0, i - distancia)
            end = min(n, i + distancia + 1)
            for j in range(start, end):
                if individuos[j] == 'L':
                    max_thieves += 1
                    individuos[j] = 'C'  # Mark the caught thief
                    break
    return max_thieves