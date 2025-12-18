"""
QUESTION:
Write a function `delete_corrupted_entries` that deletes corrupted entries from the `story_category` table. The corrupted entries are the ones where the `category_id` does not exist in the `category` table. The function should return the number of rows deleted. The function cannot use a subquery in the `WHERE` or `SET` clause of the `DELETE` statement that references the `story_category` table itself.
"""

def delete_corrupted_entries(story_category, category):
    """
    Deletes corrupted entries from the story_category table.
    
    Corrupted entries are the ones where the category_id does not exist in the category table.
    
    Args:
        story_category (list of dictionaries): The story_category table.
        category (list of dictionaries): The category table.
        
    Returns:
        int: The number of rows deleted.
    """
    # Get all the category ids present in the category table
    valid_category_ids = [cat['id'] for cat in category]
    
    # Get the ids of the corrupted entries
    corrupted_ids = [entry['category_id'] for entry in story_category if entry['category_id'] not in valid_category_ids]
    
    # Delete the corrupted entries
    deleted_count = 0
    for entry in story_category[:]:
        if entry['category_id'] in corrupted_ids:
            story_category.remove(entry)
            deleted_count += 1
            
    return deleted_count