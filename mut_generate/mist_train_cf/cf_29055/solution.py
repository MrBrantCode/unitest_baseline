"""
QUESTION:
Implement a function `transition_hsv` that takes in the current HSV values (hue, saturation, brightness) and target HSV values (target_hue, target_saturation, target_brightness). The function should return a list of steps as strings describing the actions needed to transition from the current state to the target state, with possible actions being "Change hue to <value>", "Change saturation to <value>", and "Change brightness to <value>". The function should prioritize efficiency and smooth transition.
"""

def transition_hsv(hue, saturation, brightness, target_hue, target_saturation, target_brightness):
    steps = []
    
    if hue != target_hue:
        steps.append(f"Change hue to {target_hue}")
    
    if saturation != target_saturation:
        steps.append(f"Change saturation to {target_saturation}")
    
    if brightness != target_brightness:
        steps.append(f"Change brightness to {target_brightness}")
    
    return steps