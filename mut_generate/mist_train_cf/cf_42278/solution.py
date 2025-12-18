"""
QUESTION:
Implement a Python function `process_tv_shows(data)` that takes a list of tuples as input, where each tuple contains three elements: show_type, title, and data. The function should return a dictionary with show_type as keys and a dictionary containing 'count' and 'titles' as values. The 'count' key should store the number of occurrences of each show_type and the 'titles' key should store a list of titles corresponding to each show_type. The function should handle three types of show_type: 'imdb', 'slug', or 'trakt'.
"""

def process_tv_shows(data):
    show_info = {}
    
    for show_type, title, _ in data:
        if show_type not in show_info:
            show_info[show_type] = {'count': 1, 'titles': [title]}
        else:
            show_info[show_type]['count'] += 1
            show_info[show_type]['titles'].append(title)
    
    return show_info