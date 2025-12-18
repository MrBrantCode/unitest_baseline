"""
QUESTION:
You are given a string `s` of lowercase English letters and an array `widths` denoting how many pixels wide each lowercase English letter is. Write a function `numberOfLines` that returns an array `result` of length 3 where:
- `result[0]` is the total number of lines.
- `result[1]` is the width of the last line in pixels.
- `result[2]` is the maximum number of unique characters that can be written on a single line without exceeding the 100 pixels limit.

Restrictions:
- `widths.length == 26`
- `2 <= widths[i] <= 100`
- `1 <= s.length <= 1000`
- `s` contains only lowercase English letters.
"""

def numberOfLines(widths, s):
  lines = 1
  width = 0
  unique_chars = set()
  max_unique_chars = 0

  for ch in s:
    w = widths[ord(ch) - ord('a')]
    if width + w > 100:
      lines += 1
      width = 0
      max_unique_chars = max(max_unique_chars, len(unique_chars))
      unique_chars = set()
    width += w
    unique_chars.add(ch)

  max_unique_chars = max(max_unique_chars, len(unique_chars))
  return [lines, width, max_unique_chars]