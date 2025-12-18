"""
QUESTION:
Write a function `generate_html_table` that takes a list of dictionaries (`person_list`) and the number of rows per page (`rows_per_page`) as input. Each dictionary in `person_list` represents a person with 'name' and 'age' keys. The function should generate an HTML table with a border, a caption "Person Details", and alternating background colors for each row. Only include people with an age of 18 or above in the table. The table should be paginated with `rows_per_page` rows per page and have a navigation bar for switching between pages.
"""

def generate_html_table(person_list, rows_per_page):
    # Filter people whose age is greater than or equal to 18
    filtered_person_list = [person for person in person_list if person['age'] >= 18]
    
    # Calculate the number of pages needed
    num_pages = len(filtered_person_list) // rows_per_page + 1
    
    html = '<table border="1">'
    
    # Table caption
    html += '<caption>Person Details</caption>'
    
    # Table header
    html += '<tr><th>Name</th><th>Age</th></tr>'
    
    # Generate table rows with alternating background colors
    for i, person in enumerate(filtered_person_list):
        if i % 2 == 0:
            html += '<tr style="background-color: #f2f2f2;">'
        else:
            html += '<tr>'
        html += '<td>{}</td><td>{}</td>'.format(person['name'], person['age'])
        html += '</tr>'
        
    html += '</table>'
    
    # Generate navigation bar for pagination
    html += '<div>'
    for page in range(1, num_pages + 1):
        html += '<a href="#page-{}">Page {}</a>'.format(page, page)
        if page != num_pages:
            html += ' | '
    html += '</div>'
    
    return html