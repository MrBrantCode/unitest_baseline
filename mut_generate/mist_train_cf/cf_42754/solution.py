"""
QUESTION:
Implement a function `process_results` that takes a list of patient results as input, where each result is a dictionary containing a `pid` (Patient ID) and a list of dictionaries representing predicted boxes for different ROIs. Each ROI dictionary contains the predicted box coordinates and class targets. The function should calculate the average number of predicted boxes per patient across all ROIs, identify the patient with the highest number of predicted boxes and return their `pid`, and calculate the total number of unique class targets across all predicted boxes. The function should return a tuple containing the average number of predicted boxes per patient, the `pid` of the patient with the highest number of predicted boxes, and the total number of unique class targets. The input list of patient results is expected to be a list of dictionaries with the following structure: `{'pid': ..., 'boxes': [...]}`.
"""

def process_results(patient_results):
    """
    Process patient results and return the average number of predicted boxes per patient,
    the pid of the patient with the highest number of predicted boxes, and the total
    number of unique class targets.

    Args:
    patient_results (list): A list of dictionaries containing patient results.

    Returns:
    tuple: A tuple containing the average number of predicted boxes per patient,
           the pid of the patient with the highest number of predicted boxes, and
           the total number of unique class targets.
    """

    # Initialize variables to store the total number of predicted boxes, the patient
    # with the highest number of predicted boxes, and the set of unique class targets
    total_boxes = 0
    max_boxes_pid = None
    max_boxes = 0
    unique_class_targets = set()

    # Iterate through each patient result
    for result in patient_results:
        # Extract the patient id and the list of predicted boxes
        pid = result['pid']
        boxes = result['boxes']

        # Update the total number of predicted boxes
        total_boxes += len(boxes)

        # Update the patient with the highest number of predicted boxes
        if len(boxes) > max_boxes:
            max_boxes = len(boxes)
            max_boxes_pid = pid

        # Update the set of unique class targets
        for box in boxes:
            unique_class_targets.update(box['class_targets'])

    # Calculate the average number of predicted boxes per patient
    avg_boxes_per_patient = total_boxes / len(patient_results)

    # Return the average number of predicted boxes per patient, the pid of the patient
    # with the highest number of predicted boxes, and the total number of unique class targets
    return avg_boxes_per_patient, max_boxes_pid, len(unique_class_targets)