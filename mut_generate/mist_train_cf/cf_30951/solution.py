"""
QUESTION:
Implement a function named `parse_search_results` that takes in three parameters: `output`, `repository_name`, and `is_duplicate`. The `output` parameter is a string containing search results, `repository_name` is a string representing the name of the repository to search for duplicates, and `is_duplicate` is a boolean indicating whether the search is for duplicate repositories.

The function should return a tuple `(results, count)` where `results` is a dictionary containing the details of the duplicate repositories found, and `count` is an integer representing the count of duplicate repositories found in the search results.

The `results` dictionary should have repository names as keys and dictionaries containing the source of the repository ('bitbucket' or 'github') and the file contents of the duplicate repository as values.

Note: Although the `is_duplicate` parameter is required, its value does not affect the function's behavior in the given implementation.
"""

def parse_search_results(output, repository_name, is_duplicate):
    results = {}
    count = 0

    if repository_name in output:
        lines = output.split('\n')
        for line in lines:
            if repository_name in line:
                source, file_contents = line.split(':')[-2], line.split(':')[-1].strip()
                results[repository_name] = {'source': source, 'file_contents': file_contents}
                count += 1

    return results, count