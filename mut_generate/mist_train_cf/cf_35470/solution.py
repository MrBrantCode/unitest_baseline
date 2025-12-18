"""
QUESTION:
Create a function `organize_layout_data(layout_data)` that takes a list of layout data entries, where each entry is a tuple containing a group name, layout type, and parent component. The function should return a dictionary where the keys are parent components, and the values are dictionaries with layout types as keys and lists of corresponding group names as values. The function should handle cases where a parent component or layout type is not already present in the dictionary, and it should append group names to the corresponding lists if they are already present.
"""

def organize_layout_data(layout_data):
    organized_data = {}
    for entry in layout_data:
        group_name, layout_type, parent_component = entry
        if parent_component not in organized_data:
            organized_data[parent_component] = {layout_type: [group_name]}
        else:
            if layout_type not in organized_data[parent_component]:
                organized_data[parent_component][layout_type] = [group_name]
            else:
                organized_data[parent_component][layout_type].append(group_name)
    return organized_data