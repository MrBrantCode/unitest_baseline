"""
QUESTION:
Create a function `extractBodyContent` that takes a string representing a Blade template as input and returns the content within the `@section('body')` directive, excluding the directive itself and any surrounding HTML tags. The function should return an empty string if the directive is not found.
"""

import re

def extractBodyContent(blade_template: str) -> str:
    body_content = re.search(r"@section\('body'\)\s*([\s\S]*?)@endsection", blade_template)
    if body_content:
        return body_content.group(1).strip()
    else:
        return ""