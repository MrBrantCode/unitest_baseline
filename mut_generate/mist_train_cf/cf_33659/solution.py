"""
QUESTION:
Create a function `convert_to_markdown(cell)` that takes a Jupyter notebook cell as input. If the cell type is 'code', change the cell type to 'markdown', and modify the source to include a heading based on the 'level' attribute (defaulting to 1 if not present). If the cell type is 'raw', change the cell type to 'markdown' without modifying the content. Return the modified cell.
"""

def entrance(cell):
    """
    Convert Jupyter notebook cell to Markdown format based on cell type and attributes.

    Args:
    cell: dict - The Jupyter notebook cell to be processed.

    Returns:
    dict: The modified cell after applying the appropriate conversion.
    """
    if cell['cell_type'] == 'code':
        level = cell.get('level', 1)
        cell['cell_type'] = 'markdown'
        cell['source'] = '#' * level + ' ' + cell['source']
    elif cell['cell_type'] == 'raw':
        cell['cell_type'] = 'markdown'
    return cell