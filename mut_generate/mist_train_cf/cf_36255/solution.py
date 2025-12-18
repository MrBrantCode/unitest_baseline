"""
QUESTION:
Write a function `parseRepositoryURL` that takes a string `repositoryURL` as input and returns a tuple of two strings: the repository name and the author's username. The repository URL is in the format `<reponame><authorname>/<modulename>`, where the `<reponame><authorname>` part and `<modulename>` are separated by a forward slash. The function should split the repository URL into two parts at the forward slash and return the second part as the repository name and the first part as the author's username.
"""

def parseRepositoryURL(repositoryURL):
    parts = repositoryURL.split('/')
    return parts[1], parts[0]