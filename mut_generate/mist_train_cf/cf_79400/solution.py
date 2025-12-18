"""
QUESTION:
Find the shortest traversal path (either forward or backward) to a target node in a circular doubly linked list given a reference to the current node. The function should return a tuple containing the direction of traversal and the number of steps required. If the target node is not found, return None. 

The input will be the current node and the target node's value. The circular doubly linked list is properly constructed with each node referring to the next and previous nodes correctly in a circular manner.
"""

def find_shortest_path(current, target):
    forward = current
    backward = current
    forward_count = 0
    backward_count = 0
    
    # check forward
    while True:
        if forward.data == target:
            break
        forward = forward.next
        forward_count += 1
        if forward == current:
            forward_count = -1
            break
            
    # check backward
    while True:
        if backward.data == target:
            break
        backward = backward.prev
        backward_count += 1
        if backward == current:
            backward_count = -1
            break
    
    # if target was not found in list
    if forward_count == -1 and backward_count == -1:
        return None
    
    # if target is not found in one direction 
    if forward_count == -1:
        return 'backward', backward_count
    if backward_count == -1:
        return 'forward', forward_count
    
    # if target found in both directions, return shortest path
    if forward_count < backward_count:
        return 'forward', forward_count
    else:
        return 'backward', backward_count