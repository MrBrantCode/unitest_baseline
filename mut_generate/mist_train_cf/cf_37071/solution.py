"""
QUESTION:
Implement a function `search_memory` that searches for a specific pattern within a given memory range. The function should take four parameters: `memory_start`, an integer representing the starting address of the memory range; `memory_size`, an integer representing the size of the memory range; `pattern`, a bytes object representing the pattern to be searched for; and `granularity`, an integer representing the granularity at which the search should be performed. If the pattern is found, return the memory address at which it is found. If not found, raise a `PatternNotFound` exception. If any other exception occurs, catch it, print "Swallowed LookupError", and re-raise the exception.
"""

class PatternNotFound(Exception):
    pass

def search_memory(memory_start, memory_size, pattern, granularity, memory):
    try:
        for i in range(0, memory_size, granularity):
            if pattern in memory[memory_start + i:memory_start + i + len(pattern)]:
                return memory_start + i
        raise PatternNotFound("Pattern not found in the specified memory range")
    except LookupError:
        print('Swallowed LookupError')
        raise