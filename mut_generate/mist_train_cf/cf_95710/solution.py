"""
QUESTION:
Write a function called `remove_comments` that takes a string `html` as input and returns the string with all HTML comments removed. The function must use recursion and cannot use built-in HTML parsing libraries or regular expressions. It must also handle nested HTML comments.
"""

def remove_comments(html):
    start_comment = "<!--"
    end_comment = "-->"

    def remove_single_comment(html):
        start = html.find(start_comment)
        if start == -1:
            return html

        end = html.find(end_comment, start + len(start_comment))
        if end == -1:
            return html

        return html[:start] + remove_single_comment(html[end + len(end_comment):])

    while True:
        new_html = remove_single_comment(html)
        if new_html == html:
            break
        html = new_html

    return html