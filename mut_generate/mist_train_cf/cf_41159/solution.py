"""
QUESTION:
Implement the function `process_articles(articles)` that takes a dictionary `articles` as input and returns a tuple containing a subset of articles and the total number of hits. The function should follow these rules:

- If the status of the articles is not 'OK', return a subset of the articles and the total number of hits. If the number of articles is greater than 5, return the first 5 articles. Otherwise, return all articles.
- If the status of the articles is 'OK', return an empty list and the total number of hits.

Assume the input dictionary `articles` has the following structure: `{'status': str, 'response': {'docs': List[dict], 'meta': {'hits': int}}}`.

Return type: `Tuple[List[dict], int]`
"""

from typing import List, Tuple, Dict

def process_articles(articles: Dict) -> Tuple[List[Dict], int]:
    if articles['status'] != 'OK':
        num_of_articles = len(articles['response']['docs'])
        return articles['response']['docs'][:min(num_of_articles, 5)], articles['response']['meta']['hits']
    else:
        return [], articles['response']['meta']['hits']