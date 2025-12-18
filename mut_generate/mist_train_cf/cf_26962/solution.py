"""
QUESTION:
Implement a `check_file_integrity` function that verifies the integrity of downloaded files in a BitTorrent client. The function should take two inputs: a dictionary `info` containing metadata about the torrent, including the piece length, pieces, file information, and the torrent name; and a string `datadir` representing the directory where the torrent's files are stored. The function should return a list of tuples, where each tuple contains the file path and a boolean indicating whether the file passed the integrity check. The function should handle single file torrents and multi-file torrents. The integrity check should be performed by comparing the hash values of the downloaded files with the expected hash values provided in the `pieces` list within the `info` dictionary.
"""

import hashlib
import pathlib

def check_file_integrity(info, datadir):
    piece_len = info['piece length']
    pieces = info['pieces']
    torrent_name = info['name']
    file_infos = info.get('files', [info])

    results = []
    for i, file_info in enumerate(file_infos):
        file_path = pathlib.Path(datadir, *file_info['path'])
        file_data = file_path.read_bytes()
        expected_hash = pieces[i * 20:(i + 1) * 20]  # Each 20 bytes of the hash represent the hash for the file
        file_hash = hashlib.sha1(file_data).digest()
        results.append((str(file_path), file_hash == expected_hash))

    return results