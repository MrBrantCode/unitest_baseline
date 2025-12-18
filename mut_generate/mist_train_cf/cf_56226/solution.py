"""
QUESTION:
Create a function `generate_slug` that takes a title string as input and returns a URL-friendly slug. The generated slug should be in lowercase, replace spaces with hyphens, and be unique by comparing it with a list of existing slugs. If the generated slug is not unique, append an incrementing number to the base slug until it is unique.
"""

def generate_slug(title, existing_slugs):
    slug = title.lower().replace(' ', '-')
    base_slug = slug
    i = 1
    while slug in existing_slugs:
        slug = base_slug + '-' + str(i)
        i += 1
    return slug