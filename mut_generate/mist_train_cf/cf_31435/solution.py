"""
QUESTION:
Create a function named `generate_collapsible_list` that takes a list of item categories as input, where each category contains a title and a list of items, and each item has an id and a title. The function should return the HTML code for a collapsible list, following the specified structure and classes. The input list should be in the format:
```python
item_categories = [
    {
        "title": "category_title",
        "items": [
            {"id": item_id, "title": "item_title"},
            ...
        ]
    },
    ...
]
```
The output HTML code should include a collapsable list with links to each category and item. The category links should be in the format `#category_titleItems` and the item links should be in the format `#itemitem_id`.
"""

def generate_collapsible_list(item_categories):
    html_code = '<div>\n'
    html_code += '  <li class="collapsable startCollapsed"><strong>Items</strong> <a href="/item/add">+</a></li>\n'
    
    for category in item_categories:
        html_code += '  <div>\n'
        html_code += f'    <li class="section"><a href="#{category["title"]}Items">{category["title"]} Items</a></li>\n'
        for item in category["items"]:
            html_code += f'    <li class="subsection"><a href="#item{item["id"]}">{item["title"]}</a></li>\n'
        html_code += '  </div>\n'
    
    html_code += '</div>'
    return html_code