"""
QUESTION:
Write a function named `generate_html_table` that takes a list of dictionaries (`person_list`) and the number of rows per page (`rows_per_page`) as input. The dictionaries in `person_list` represent people with the keys 'name' and 'age'. The function should return an HTML table with a border, a caption that says "Person Details", and each row should have alternating background colors. The table should only include people whose age is greater than or equal to 18 and should be paginated with `rows_per_page` rows per page. Each page should have a navigation bar to switch between pages.
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