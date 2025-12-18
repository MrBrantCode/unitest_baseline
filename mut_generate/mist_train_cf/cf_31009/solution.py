"""
QUESTION:
Create a function `get_ownership_permission_policy` that takes a list of video objects and the user's role as input and returns a dictionary containing the ownership permission policy for each video. The ownership permission policy is determined based on the video's ownership status and the user's role. The video object has two attributes: `title` and `ownership_status`. The user's role can be "admin", "editor", or "viewer", and the ownership status can be "owned", "shared", or "public". The ownership permission policy is determined as follows:
- If the user is an admin, they have full permission for all videos regardless of ownership status.
- If the user is an editor, they have full permission for "owned" videos, read-only permission for "shared" videos, and no permission for "public" videos.
- If the user is a viewer, they have read-only permission for "owned" and "shared" videos, and no permission for "public" videos.
"""

def get_ownership_permission_policy(videos, user_role):
    permission_policy = {}
    for video in videos:
        if user_role == "admin":
            permission_policy[video.title] = "full"
        elif user_role == "editor":
            if video.ownership_status == "owned":
                permission_policy[video.title] = "full"
            elif video.ownership_status == "shared":
                permission_policy[video.title] = "read-only"
            else:
                permission_policy[video.title] = "no-permission"
        elif user_role == "viewer":
            if video.ownership_status in ["owned", "shared"]:
                permission_policy[video.title] = "read-only"
            else:
                permission_policy[video.title] = "no-permission"
    return permission_policy