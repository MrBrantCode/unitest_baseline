"""
QUESTION:
## Description

You've been working with a lot of different file types recently as your interests have broadened.

But what file types are you using the most? With this question in mind we look at the following problem.

Given a `List/Array` of Filenames (strings) `files` return a `List/Array of string(s)` contatining the most common extension(s). If there is a tie, return a sorted list of all extensions.

### Important Info:

* Don't forget, you've been working with a lot of different file types, so expect some interesting extensions/file names/lengths in the random tests.
* Filenames and extensions will only contain letters (case sensitive), and numbers.
* If a file has multiple extensions (ie: `mysong.mp3.als`) only count the the last extension (`.als` in this case)


## Examples

```
files = ['Lakey - Better days.mp3', 
         'Wheathan - Superlove.wav', 
         'groovy jam.als', 
         '#4 final mixdown.als', 
         'album cover.ps', 
         'good nights.mp3']
```

would return: `['.als', '.mp3']`, as both of the extensions appear two times in files.

```
files = ['Lakey - Better days.mp3', 
         'Fisher - Stop it.mp3', 
         'Fisher - Losing it.mp3', 
         '#4 final mixdown.als', 
         'album cover.ps', 
         'good nights.mp3']
```
would return `['.mp3']`, because it appears more times then any other extension, and no other extension has an equal amount of appearences.
"""

from collections import Counter
import re

def most_common_extensions(files):
    # Extract extensions using regex
    extensions = [re.match(r'.*(\.[^.]+)$', fn).group(1) for fn in files if re.match(r'.*(\.[^.]+)$', fn)]
    
    # Count the occurrences of each extension
    extension_counts = Counter(extensions)
    
    # Find the maximum count
    max_count = max(extension_counts.values(), default=0)
    
    # Collect all extensions that have the maximum count
    most_common = [ext for ext, count in extension_counts.items() if count == max_count]
    
    # Return the sorted list of most common extensions
    return sorted(most_common)