"""
QUESTION:
Write a function `generate_pagination` that takes three parameters: `current_page`, `total_pages`, and `max_visible_pages`. The function should return a list of page numbers and/or strings representing the page numbers to display, including the current page and placeholders for skipped pages. The list should be limited to `max_visible_pages` in length and include the current page. The function should handle cases where `total_pages` is less than or equal to `max_visible_pages` and where `current_page` is near the start or end of the pagination.
"""

from typing import List, Union

def generate_pagination(current_page: int, total_pages: int, max_visible_pages: int) -> List[Union[int, str]]:
    if total_pages <= max_visible_pages:
        return list(range(1, total_pages + 1))
    
    half_visible = max_visible_pages // 2
    if current_page <= half_visible + 1:
        pages = list(range(1, max_visible_pages - 1)) + ['...', total_pages]
    elif current_page >= total_pages - half_visible:
        pages = [1, '...'] + list(range(total_pages - max_visible_pages + 3, total_pages + 1))
    else:
        pages = [1, '...']
        start = current_page - half_visible
        end = current_page + half_visible
        for i in range(start, end + 1):
            pages.append(i)
        pages.append('...')
        pages.append(total_pages)
    
    return pages