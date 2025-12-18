"""
QUESTION:
Implement a function `dragGestureDetector` that enables dragging a grid of items by clicking down on or outside the item and then dragging into it. The detector should track the gesture and recognize move events even if the initial down event occurs outside the item.
"""

def dragGestureDetector(event):
    """
    Detects and tracks drag gestures on a grid of items.

    Args:
        event (dict): The event object containing information about the gesture.

    Returns:
        bool: True if the gesture is a drag event, False otherwise.
    """
    # Check if the initial down event occurs outside the item
    if event['type'] == 'DOWN' and not event['item'].get('contains', False):
        # Store the initial event position
        initial_position = (event['x'], event['y'])
        
        # Check if the subsequent move events are within the item
        if event['type'] == 'MOVE' and event['item'].get('contains', False):
            # Calculate the distance between the initial and current positions
            distance = ((event['x'] - initial_position[0]) ** 2 + (event['y'] - initial_position[1]) ** 2) ** 0.5
            
            # Recognize the gesture as a drag event if the distance exceeds a certain threshold
            if distance > 10:  # Adjust the threshold value as needed
                return True
    
    return False