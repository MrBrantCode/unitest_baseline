"""
QUESTION:
Create a function `filter_matches(pattern, matches)` that takes a dictionary `pattern` and a DataFrame `matches` as input. The function should return a new DataFrame containing only the file names that either match the software packages listed in the `pattern` dictionary or do not have specific prefixes. The prefixes to be excluded are 'linux_', 'FFmpeg_', 'curl_', 'nginx_', 'openssl_', 'redis_', 'tmux_', and 'vlc_'.
"""

import pandas as pd

def filter_matches(pattern, matches):
    filtered_matches = matches[matches['file'].apply(lambda x: x in list(pattern.values()) or not (x.startswith('linux_') or x.startswith('FFmpeg_') or x.startswith('curl_') or x.startswith('nginx_') or x.startswith('openssl_') or x.startswith('redis_') or x.startswith('tmux_') or x.startswith('vlc_')))]
    return filtered_matches