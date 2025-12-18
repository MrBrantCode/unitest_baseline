"""
QUESTION:
Create a Split Form Functionality

Implement a function that mimics the behavior of Access 2007's Split Form, which combines a grid view and a form in one control. When a record is selected in the grid view, it should be displayed in the form and be editable in either view. The function should take into account synchronizing changes between the grid view and the form.
"""

def split_form(records):
    # This is a simplified representation of how the split form functionality could be implemented in Python.
    # In a real-world application, you would likely be using a GUI framework to create the form and grid views.
    
    # Create a dictionary to store the selected record
    selected_record = {}
    
    # Simulate the grid view
    grid_view = []
    for record in records:
        grid_view.append(record)
    
    # Simulate the form view
    form_view = selected_record
    
    # Function to select a record in the grid view and update the form view
    def select_record(index):
        nonlocal selected_record
        selected_record = grid_view[index]
        return selected_record
    
    # Function to update a field in the form view and update the grid view
    def update_record(field, value):
        nonlocal selected_record
        selected_record[field] = value
        for i, record in enumerate(grid_view):
            if record == selected_record:
                grid_view[i] = selected_record
        return selected_record
    
    return select_record, update_record