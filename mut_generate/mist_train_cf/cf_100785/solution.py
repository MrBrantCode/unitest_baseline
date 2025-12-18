"""
QUESTION:
Create a function named `generate_book_review_html` that takes four parameters: `title`, `author`, `plot`, and `themes`. The function should return a string of HTML code that displays the book's title in an H1 header, the author's name in an H2 header, the plot overview in a paragraph, and the themes in an H3 header followed by a list. The themes should be separated by commas in the input string and displayed as separate list items in the output HTML.
"""

def generate_book_review_html(title, author, plot, themes):
    themes_list = themes.split(",")
    themes_html = ""
    for theme in themes_list:
        themes_html += "<li>" + theme.strip() + "</li>"
    html = "<h1>" + title + "</h1>\n<h2>By " + author + "</h2>\n<p>" + plot + "</p>\n<h3>Themes:</h3>\n<ul>\n" + themes_html + "</ul>"
    return html