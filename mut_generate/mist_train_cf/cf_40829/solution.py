"""
QUESTION:
Create a function `filter_repositories` that takes a list of strings representing GitHub repositories and a tuple representing a star count range, and returns a list of tuples containing the repository name and its corresponding star count, filtered by the specified star count range.

The repository strings are in the format `<reponame><gh_stars>`, where `<gh_stars>` represents the star count within the range of 1 to 10. The star count range tuple contains two integers representing the lower and upper bounds of the star count range, inclusive. The function should extract the repository name and star count from each repository string, filter out repositories with star counts outside the specified range, and return the filtered list of tuples.
"""

def filter_repositories(repositories: list, stars_range: tuple) -> list:
    filtered_repositories = []
    for repo in repositories:
        repo_name, star_count = repo.rsplit('/', 1)
        star_count = int(star_count[-1])  # Extract the last character as star count
        if stars_range[0] <= star_count <= stars_range[1]:
            filtered_repositories.append((repo_name, star_count))
    return filtered_repositories