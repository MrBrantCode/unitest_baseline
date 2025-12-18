"""
QUESTION:
Implement a function `extract_left_clips` that takes a list of sequencing records `normal` as input, where each record has the attributes `is_supplementary`, `is_unmapped`, `pos`, `mpos`, and `cigartuples`. The function should return a list of left clip positions for the records that are not supplementary or unmapped and are the first read in a pair, as determined by `pos` being less than `mpos`. The left clip position is the length of the first CIGAR operation with type 4 (soft clip) in the `cigartuples` list. If no such operation exists, the record is skipped.
"""

def extract_left_clips(normal):
    left_clips = []
    for rec in normal:
        if not (rec.is_supplementary or rec.is_unmapped) and rec.pos < rec.mpos:
            get_clip = lambda c: c[1] if c[0] == 4 else None
            clip_left = get_clip(rec.cigartuples[0])
            if clip_left is not None:
                left_clips.append(clip_left)
    return left_clips