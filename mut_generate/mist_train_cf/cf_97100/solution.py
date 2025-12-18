"""
QUESTION:
Create a function named `tower_of_hanoi_iterative` that takes three parameters: the number of disks, the source stack, and the target stack. Implement the function iteratively, without using recursion, to solve the Tower of Hanoi puzzle. Use stacks to keep track of the movement of the disks. The function should print each step of the solution in a readable format, such as "Move disk X from stack Y to stack Z", and return the minimum number of moves required to solve the puzzle. The function should handle any positive integer input for the number of disks, including large values, and should be able to solve the puzzle for up to 20 disks efficiently. The function should follow the rules of the Tower of Hanoi puzzle.
"""

def tower_of_hanoi_iterative(num_disks, source_stack, target_stack):
    # Create stacks for the source, auxiliary, and target
    stacks = {'A': [], 'B': [], 'C': []}
    stacks[source_stack] = list(range(1, num_disks + 1))
    
    # Calculate the minimum number of moves required
    min_moves = 2**num_disks - 1
    
    # Helper function to get the next stack in the solution
    def get_next_stack(stack1, stack2):
        if stack1 != source_stack and stack2 != source_stack:
            return source_stack
        elif stack1 != target_stack and stack2 != target_stack:
            return target_stack
        else:
            return 'B'
    
    # Initialize the current step and move count
    step = 1
    moves = 0
    
    # Iterate until all disks are moved to the target stack
    while len(stacks[target_stack]) != num_disks:
        # Check if it's an odd or even step
        if step % 2 == 1:
            # Odd step: Move the smallest disk
            if not stacks[source_stack]:
                # If the source stack is empty, swap the auxiliary and target stacks
                source_stack, target_stack = target_stack, source_stack
            else:
                # Move the smallest disk from the source stack to the target stack
                disk = stacks[source_stack].pop()
                stacks[target_stack].append(disk)
                moves += 1
                print(f"Move disk {disk} from stack {source_stack} to stack {target_stack}")
        else:
            # Even step: Move a larger disk
            for stack in ['A', 'B', 'C']:
                if stack != source_stack and stack != target_stack and stacks[stack]:
                    # Move the top disk from the non-source and non-target stack
                    disk = stacks[stack].pop()
                    stacks[get_next_stack(source_stack, target_stack)].append(disk)
                    moves += 1
                    print(f"Move disk {disk} from stack {stack} to stack {get_next_stack(source_stack, target_stack)}")
                    break
        
        # Increment the step count
        step += 1
    
    # Print the minimum number of moves required
    print(f"Minimum number of moves: {min_moves}")
    
    # Return the minimum number of moves required
    return min_moves