"""
QUESTION:
Write a function `generate_readme` that takes the following parameters:
- `author`: A string representing the author's name.
- `author_email`: A string representing the author's email.
- `license`: A string representing the package's license.
- `url`: A string representing the package's URL.
- `description`: A string representing the brief package description.
- `long_description`: A string representing the detailed package description.
- `classifiers`: A list of strings representing the package classifiers.

The function should return a string representing the content of a README file in Markdown format, following Python package documentation conventions, using the provided information.
"""

def generate_readme(author, author_email, license, url, description, long_description, classifiers):
    readme_content = f"# Package Name\n\n{description}\n\n## Installation\n\nUse the package manager [pip]({url}) to install package-name.\n\n```bash\npip install package-name\n```\n\n## Usage\n\n```python\nimport package_name\n\npackage_name.do_something()\n```\n\n## License\n[{license}]({url})\n\n## Author\n{author}\n{author_email}\n\n## Development Status\n{classifiers[0]}\n\n## Classifiers\n"
    
    for classifier in classifiers:
        readme_content += f"- {classifier}\n"
    
    return readme_content