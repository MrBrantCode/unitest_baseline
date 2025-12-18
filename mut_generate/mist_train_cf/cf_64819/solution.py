"""
QUESTION:
Write a function called `perfectPlay` that determines the winning move for the game of Nim. The game involves `n` heaps with sizes represented by the list `heap`. The function should return a string indicating the winning move if the first player can win, or a message stating that the first player will lose if the second player plays perfectly. The function should not take any other parameters besides `n` and `heap`.
"""

def perfectPlay(n, heap):
    xor_sum = 0
    for i in range(n):
        xor_sum = xor_sum ^ heap[i]
    
    if xor_sum == 0:
        return "Player who plays first will lose in a perfect gameplay."
    else:
        # Iterate over heaps to find the desired heap
        for i in range(n):
            desired_heap = xor_sum ^ heap[i]
            
            if desired_heap < heap[i]:
                return f"Player who plays first should remove {heap[i]-desired_heap} from heap {i+1} to win."