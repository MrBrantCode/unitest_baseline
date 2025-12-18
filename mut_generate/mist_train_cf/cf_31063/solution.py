"""
QUESTION:
Implement a method `generate_tweet` for the `TwitterClient` class that takes a repository's full name, description, language, and issues URL as input and returns a formatted tweet. The tweet should be formatted using a template with the following structure: "$repo_full_name - $repo_desc.\n\nLanguage: $language\nIssues: $issues_url". The method should substitute the placeholders in the template with the actual values.
"""

def generate_tweet(repo_full_name, repo_desc, language, issues_url):
    TWEET_TEMPLATE = Template(
        "$repo_full_name - $repo_desc.\n\nLanguage: $language\nIssues: $issues_url"
    )
    tweet = TWEET_TEMPLATE.substitute(
        repo_full_name=repo_full_name,
        repo_desc=repo_desc,
        language=language,
        issues_url=issues_url
    )
    return tweet