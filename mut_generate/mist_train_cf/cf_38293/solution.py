"""
QUESTION:
Create a function `extract_filename_from_ftp_url(url)` that takes a string `url` representing an FTP URL in the format `ftp://<hostname>/<filename>` and returns the extracted filename. The filename may contain alphanumeric characters, underscores, dots, and other valid filename characters. The FTP URL will always follow the specified format.
"""

def extract_filename_from_ftp_url(url):
    # Split the URL by '/' and extract the last element as the filename
    filename = url.split('/')[-1]
    return filename