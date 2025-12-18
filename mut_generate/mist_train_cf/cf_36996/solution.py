"""
QUESTION:
Implement the `averageJointDistance` method in the `Visualization` class. The method should calculate the average distance between all pairs of joints in the skeleton using the Euclidean distance formula and return the result. The Euclidean distance between two joints can be calculated as `distance = sqrt((x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2)`, where `(x1, y1, z1)` and `(x2, y2, z2)` are the 3D coordinates of the two joints. You can access the skeleton's joints and their coordinates using the `self._visualization.skeleton.get_joint_coordinates()` method, which returns a dictionary where the keys are joint names and the values are tuples of the form `(x, y, z)` representing the 3D coordinates of the joint. The average distance should be calculated for all pairs of joints, not just adjacent ones.
"""

def averageJointDistance(joint_coordinates):
    """
    Calculate the average distance between all pairs of joints in the skeleton.

    Args:
    joint_coordinates (dict): A dictionary where the keys are joint names and the values are tuples of the form (x, y, z) representing the 3D coordinates of the joint.

    Returns:
    float: The average distance between all pairs of joints in the skeleton.
    """
    num_joints = len(joint_coordinates)
    total_distance = 0
    num_pairs = 0
    for joint1 in joint_coordinates:
        for joint2 in joint_coordinates:
            if joint1 != joint2:
                x1, y1, z1 = joint_coordinates[joint1]
                x2, y2, z2 = joint_coordinates[joint2]
                distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
                total_distance += distance
                num_pairs += 1
    if num_pairs > 0:
        return total_distance / num_pairs
    else:
        return 0