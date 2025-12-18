"""
QUESTION:
Create a function `create_work_item` that takes in a list of child work item IDs, a unique positive integer ID for the new work item, and a non-empty string title for the new work item. The function should return a message indicating the successful creation of the work item with the given ID and title, and its association with the specified child work items.
"""

def create_work_item(child_work_item_ids, id, title):
    new_work_item = {
        "id": id,
        "title": title,
        "child_work_items": child_work_item_ids
    }
    
    for child_id in child_work_item_ids:
        # Associate the new work item with the child work item using the project management system's API or database operations
        # This step will depend on the specific implementation of the project management system
        
        # For demonstration purposes, print a message indicating the association
        print(f"Work item with ID {id} associated with child work item {child_id}.")
    
    return f"Work item with ID {id} and title '{title}' created and associated with child work items {child_work_item_ids}."