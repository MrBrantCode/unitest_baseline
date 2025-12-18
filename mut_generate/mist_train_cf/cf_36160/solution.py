"""
QUESTION:
Implement a function `extractContent` that takes a string `htmlSnippet` as input. The function should extract and return the content between the `</div>` and `</x-app-layout>` tags in `htmlSnippet`. If the `</div>` tag is not found before the `</x-app-layout>` tag, the function should return an empty string.
"""

def extractContent(htmlSnippet):
    div_end_index = htmlSnippet.find("</div>")
    app_layout_index = htmlSnippet.find("</x-app-layout>")
    
    if div_end_index != -1 and app_layout_index != -1:
        return htmlSnippet[div_end_index + len("</div>"):app_layout_index]
    else:
        return ""