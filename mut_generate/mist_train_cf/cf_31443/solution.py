"""
QUESTION:
Implement a function `generateFilename` that takes a `sceneFile` object with a `meta` attribute containing `show`, `season`, and `episode` properties, a filename `pattern` string with placeholders for `{show}`, `{season}`, and `{episode}`, and optional boolean flags `zeroesSeason` and `zeroesEpisodes`. The function should return a filename based on the provided pattern, replacing the placeholders with the actual metadata values and formatting the season and episode numbers with leading zeroes if the corresponding flags are `True`. The filename should include the original file extension.
"""

def generateFilename(sceneFile, pattern, zeroesSeason=False, zeroesEpisodes=False):
    meta = sceneFile.meta
    extension = os.path.splitext(sceneFile.file)[1]
    episodeString = ('%02d' if zeroesEpisodes else '%d') % meta.episode
    seasonString = ('%02d' if zeroesSeason else '%d') % meta.season
    filename = pattern.replace('{show}', meta.show)
    filename = filename.replace('{season}', seasonString)
    filename = filename.replace('{episode}', episodeString)
    filename += extension
    return filename