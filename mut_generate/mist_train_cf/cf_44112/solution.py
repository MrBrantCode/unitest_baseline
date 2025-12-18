"""
QUESTION:
You are given a series of video clips from a sporting event that lasted `T` seconds. Each video clip `clips[i]` is an interval: it starts at time `clips[i][0]` and ends at time `clips[i][1]`. Implement a function `videoStitching(clips, T)` that returns the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event (`[0, T]`). If the task is impossible, return `-1`. Additionally, return the specific clips used in the optimal solution. 

Note that `1 <= clips.length <= 100`, `0 <= clips[i][0] <= clips[i][1] <= 100`, and `0 <= T <= 100`.
"""

def videoStitching(clips, T):
    clips.sort(key=lambda x: (x[0], -x[1]))
    clips_used = []
    end, cnt, i=0, 0, 0

    while end < T:
        maxEnd = end
        while i < len(clips) and clips[i][0] <= end:
            maxEnd = max(maxEnd, clips[i][1])
            i += 1

        if end == maxEnd: return -1
        end = maxEnd
        cnt += 1
        clips_used.append(clips[i-1])

    return cnt, clips_used