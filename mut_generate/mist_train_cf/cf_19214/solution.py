"""
QUESTION:
Implement a function `ItemsTableViewController` that creates a table view to display a list of custom items with properties (name, price, quantity, description, image). Each item should be displayed in a custom cell and allow the user to view details and edit properties upon tapping on the cell. The table view should also support swipe gestures for deletion and have a search bar at the top to filter items by name.
"""

def ItemsTableViewController(items, search_text=""):
    # Create a filtered list of items based on the search text
    filtered_items = [item for item in items if search_text.lower() in item['name'].lower()]
    
    # Create a table view to display the filtered items
    table_view = []
    
    # Populate the table view with the filtered items
    for item in filtered_items:
        table_view.append({
            'name': item['name'],
            'price': item['price'],
            'quantity': item['quantity'],
            'description': item['description'],
            'image': item['image']
        })
    
    return table_view