"""
QUESTION:
Write a function `generate_html_table` that takes a list of dictionaries representing top 10 bestselling books in a specific genre. Each dictionary contains the keys 'id', 'title', 'author', 'genre', and 'sales'. The function should return a string representing an HTML table displaying the information of these books. The table should have columns for 'ID', 'Title', 'Author', 'Genre', and 'Sales'.
"""

def generate_html_table(bestselling_books):
    html = '<table>\n'
    html += '<tr><th>ID</th><th>Title</th><th>Author</th><th>Genre</th><th>Sales</th></tr>\n'

    for book in bestselling_books:
        html += '<tr>'
        html += '<td>{}</td>'.format(book["id"])
        html += '<td>{}</td>'.format(book["title"])
        html += '<td>{}</td>'.format(book["author"])
        html += '<td>{}</td>'.format(book["genre"])
        html += '<td>{}</td>'.format(book["sales"])
        html += '</tr>\n'

    html += '</table>'
    return html