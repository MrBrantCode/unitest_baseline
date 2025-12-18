"""
QUESTION:
Write a function named time_needed_to_fill_bottles that calculates the time in minutes needed to process and fill a batch of bottles. The machine's rate is 200 bottles per 12 minutes. The function should take the batch size (number of bottles) as input and return the time needed in minutes.
"""

def time_needed_to_fill_bottles(num_bottles):
    # Number of bottles filled per minute
    rate = 200 / 12
    
    # Time needed to fill 'num_bottles'
    time_needed = num_bottles / rate
    
    return time_needed