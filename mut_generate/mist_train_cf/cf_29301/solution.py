"""
QUESTION:
Write a function `comment_manipulation(body, comment_format, content)` that takes a string `body` representing the body of text, a list of strings `comment_format` representing the comment formats, and a string `content` representing the content in which the body of text will be inserted. The function should return the updated `body` if it needs to be modified to match the `comment_format`, or "No modification needed" if the trimmed `body` exists within the trimmed `content`. The function should apply the comment formats as follows: if the length of `comment_format` is 1, insert the comment format at the beginning of each line in `body`; if the length of `comment_format` is 2, insert the first comment format at the beginning and the second comment format at the end of `body`. The function should then compare the trimmed `body` with the trimmed `content` after removing any extra spaces.
"""

def comment_manipulation(body, comment_format, content):
    if len(comment_format) == 1:
        split_body = body.splitlines(True)
        mod_body = (comment_format[0] + ' ').join(['', *split_body])
    elif len(comment_format) == 2:
        mod_body = comment_format[0] + '\n' + body.rstrip() + '\n' + comment_format[1]
    trimmed_body = ' '.join(body.split())
    trimmed_file = ' '.join(content.replace(comment_format[0], '').split())
    if trimmed_body not in trimmed_file:
        return mod_body
    else:
        return "No modification needed"