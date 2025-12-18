"""
QUESTION:
Create a function `count_unique_requests(url_requests)` that takes a list of URL requests as input and returns a list of tuples containing unique URLs and their corresponding request counts. The function should ignore query parameters in the URLs, count the total number of requests for each unique URL, and sort the URLs in descending order based on their request count. The implementation should use a single loop and avoid built-in functions or libraries for sorting or counting.
"""

def count_unique_requests(url_requests):
    url_count = {}  

    for request in url_requests:
        url, _, _ = request.partition('?')  
        if url in url_count:
            url_count[url] += 1
        else:
            url_count[url] = 1

    sorted_urls = []  

    while url_count:
        max_count = -1
        max_url = ""
        for url, count in url_count.items():
            if count > max_count:
                max_count = count
                max_url = url
        sorted_urls.append((max_url, max_count))
        del url_count[max_url]

    return sorted_urls