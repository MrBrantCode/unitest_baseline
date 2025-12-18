"""
QUESTION:
Create a function that filters documents in the 'shapes' collection with an 'area' value within a specified range [200, 500], excluding values less than 300, and then groups the remaining documents by 'area' value. For each group, calculate the average and standard deviation of 'area' values. Exclude any groups with a standard deviation above 50. The function should return the grouped documents in descending order of 'area' values, limited to the first 10 documents, along with the total count of documents that meet the criteria.

The function should also include the following restrictions:
- The result should be sorted in descending order of the 'area' value.
- Only the first 10 documents should be returned.
- The function should calculate and include the average and standard deviation of 'area' values for each group.
- The function should exclude any groups where the standard deviation is above 50.
- The function should return the total count of documents that match the given criteria, excluding any groups that were excluded due to the standard deviation threshold.
"""

import numpy as np

def entrance(shapes):
    # Filter shapes within the area range [200, 500] and exclude values less than 300
    filtered_shapes = [shape for shape in shapes if 200 <= shape['area'] <= 500 and shape['area'] >= 300]

    # Group the remaining shapes by 'area' value
    groups = {}
    for shape in filtered_shapes:
        area = shape['area']
        if area not in groups:
            groups[area] = []
        groups[area].append(shape)

    # Calculate the average and standard deviation of 'area' values for each group
    results = []
    for area, group in groups.items():
        avg = np.mean([shape['area'] for shape in group])
        std_dev = np.std([shape['area'] for shape in group])
        if std_dev <= 50:
            results.append({
                'area': area,
                'documents': group,
                'avg': avg,
                'stdDev': std_dev
            })

    # Sort the results in descending order of 'area' values and limit to the first 10 documents
    results.sort(key=lambda x: x['area'], reverse=True)
    results = results[:10]

    # Calculate the total count of documents that meet the criteria
    count = sum(len(group['documents']) for group in results)

    return {
        'count': count,
        'groups': results
    }