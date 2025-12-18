"""
QUESTION:
Write a function `extractScriptUrls(html)` that takes a string `html` representing the HTML content and returns a list of unique URLs of the external JavaScript files referenced in the HTML. The function should handle both inline script tags and external script tags with various attributes. Assume the HTML content is well-formed, valid, and script tags may have attributes like `src`, `async`, `defer`, etc., and may appear in the `<head>` or `<body>` sections of the HTML.
"""

import re

def extractScriptUrls(html):
    script_urls = set()
    script_pattern = r'<script\s+[^>]*?src=["\']([^"\']+?)["\'][^>]*?>'
    inline_script_pattern = r'<script>(.*?)</script>'

    # Extract external script URLs
    script_matches = re.findall(script_pattern, html, flags=re.IGNORECASE)
    script_urls.update(script_matches)

    # Extract inline script URLs (if any)
    inline_script_matches = re.findall(inline_script_pattern, html, flags=re.DOTALL)
    for inline_script in inline_script_matches:
        if "src" in inline_script:
            inline_src_match = re.search(r'src=["\']([^"\']+?)["\']', inline_script, flags=re.IGNORECASE)
            if inline_src_match:
                script_urls.add(inline_src_match.group(1))

    return list(script_urls)