"""
QUESTION:
Create a function `generate_license_file` that takes three parameters: `kernel_protocol_version_info` (a tuple containing major and minor version numbers), `license` (a string representing the license type), and `authors` (a dictionary with author names as keys and tuples of name and email as values). The function should return a string representing a formatted license file.
"""

def generate_license_file(kernel_protocol_version_info, license, authors):
    kernel_protocol_version = "%i.%i" % kernel_protocol_version_info

    license_file = f"Kernel Protocol Version: {kernel_protocol_version}\nLicense: {license}\n\nAuthors:\n"
    for author, details in authors.items():
        author_name, author_email = details
        license_file += f"- {author}\n  Name: {author_name}\n  Email: {author_email}\n"

    return license_file