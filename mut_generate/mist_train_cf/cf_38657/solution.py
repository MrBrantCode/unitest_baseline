"""
QUESTION:
Create a function named `process_uploaded_files` that takes two parameters: `request` (a dictionary-like object containing uploaded files) and `num_files` (an integer representing the number of files to process). The function should validate each file, ensuring it exists, is a .txt file, and is not empty. If any file fails validation, return an error message with a status code of 500. If all files pass validation, return a list of decoded contents of each file. Each file's key in the `request` object is constructed as 'file' + str(x), where x is the 1-indexed file number.
"""

def process_uploaded_files(request, num_files):
    decoded_contents = []
    for x in range(1, num_files + 1):
        file_key = 'file' + str(x)
        if file_key not in request.files:
            return 'Error with attached file(s)', 500
        if not request.files.get(file_key).filename.split(".")[-1] == 'txt':
            return 'Only .txt files accepted', 500
        try:
            contents = request.files.get(file_key).read().decode("utf-8")
        except:
            return 'Error with attached file(s)', 500
        if not contents:
            return 'Error with attached file(s)', 500
        decoded_contents.append(contents)
    return decoded_contents