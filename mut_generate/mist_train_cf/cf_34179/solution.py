"""
QUESTION:
Write a function `parseFilePath` that takes a file path as input and returns a dictionary containing the directory path, file name without the extension, and the file extension. The file path will always be in the format "directory/fileName.extension" with possible multiple levels of subdirectories. The function should return a dictionary with the keys "directory", "fileName", and "extension".
"""

def parseFilePath(file_path):
    components = file_path.split('/')
    file_name, extension = components[-1].split('.')
    directory = '/'.join(components[:-1])
    return {
        "directory": directory,
        "fileName": file_name,
        "extension": extension
    }