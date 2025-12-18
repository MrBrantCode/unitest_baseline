"""
QUESTION:
Create a function `watchedVideosByFriends(watchedVideos, friends, id, level)` that takes in four parameters: a list of lists `watchedVideos` where `watchedVideos[i]` is the list of videos watched by person `i`, a list of lists `friends` where `friends[i]` is the list of friends of person `i`, a person's `id`, and a `level`. The function should return a list of videos watched by friends at the given `level` from the person with the given `id`, ordered by their frequencies in ascending order and then alphabetically. If two videos have the same frequency, order them by their popularity scores in descending order and then alphabetically. The popularity score of a video is the sum of the levels of all people who watched it.
"""

def watchedVideosByFriends(watchedVideos, friends, id, level):
    level_people = []
    queue = [(id, 0)]  # BFS with source node id and level 0
    visited = {id}    # Use set to record visited node
    while queue:
        node, node_level = queue.pop(0)
        if node_level == level:
            level_people.append(node)
        elif node_level < level:
            for j in friends[node]:
                if j not in visited:
                    visited.add(j)
                    queue.append((j, node_level+1))

    video_count = {}  # Keeps count of each video watched
    video_score = {}  # Keeps popularity score of each video
    for people in level_people:
        for video in watchedVideos[people]:
            if video not in video_count:
                video_count[video] = 1
                video_score[video] = level
            else:
                video_count[video] += 1
                video_score[video] += level

    # Sort by popularity score in descending order, then by frequency, and lastly by name.
    res = sorted(video_count.keys(), key=lambda x: (-video_score[x], video_count[x], x))
    return res