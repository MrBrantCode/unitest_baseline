"""
QUESTION:
Implement the `parseFilePath` function to extract information from a file path in the format `<filename><directory_path><gh_stars><stars_count>+` where `<filename>` consists of alphanumeric characters and underscores, `<directory_path>` consists of alphanumeric characters, slashes, and underscores, `<gh_stars>` is a tag indicating GitHub stars, and `<stars_count>` is a positive integer. Return a dictionary with keys "filename", "directory_path", and "stars_count" containing the corresponding extracted values.
"""

def parseFilePath(file_path):
    result = {}
    filename_start = file_path.rfind('/') + 1
    filename_end = file_path.find('<gh_stars>')
    stars_start = file_path.find('<gh_stars>') + len('<gh_stars>')
    stars_end = file_path.find('+')
    
    result["filename"] = file_path[filename_start:filename_end]
    result["directory_path"] = file_path[:filename_start]
    result["stars_count"] = int(file_path[stars_start:stars_end])
    
    return result