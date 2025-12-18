"""
QUESTION:
Write a function named `generate_sitemap` that takes two lists of dictionaries as input: `game_urls` and `new_urls`. Each dictionary in the lists should contain the keys "url" and "lastmod". The function should return a string representing an XML sitemap following the format specified by the sitemaps.org protocol. The sitemap should include all URLs from both lists, with a change frequency of "weekly" and a priority of 0.8 for game URLs and 0.6 for new URLs.
"""

def generate_sitemap(game_urls, new_urls):
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for game in game_urls:
        url = f'<url>\n\t<loc>{game["url"]}</loc>\n\t<lastmod>{game["lastmod"]}</lastmod>\n\t<changefreq>weekly</changefreq>\n\t<priority>0.8</priority>\n</url>\n'
        sitemap += url

    for new in new_urls:
        url = f'<url>\n\t<loc>{new["url"]}</loc>\n\t<lastmod>{new["lastmod"]}</lastmod>\n\t<changefreq>weekly</changefreq>\n\t<priority>0.6</priority>\n</url>\n'
        sitemap += url

    sitemap += '</urlset>'
    return sitemap