"""
QUESTION:
Write a function `process_committee_data(committee_data: dict) -> list` that takes a dictionary `committee_data` as input. The input dictionary contains information about committees and their associated meetings. The function should return a list of tuples, where each tuple contains the committee name and the number of meetings for which the user has permissions. The `has_perm` function, which checks the meeting permissions, is assumed to be already defined.
"""

def process_committee_data(committee_data: dict) -> list:
    result = []
    for committee_info in committee_data.get("forward_to_committee_ids", []):
        committee_name = committee_info.get("name")
        meeting_ids = committee_info.get("meeting_ids", [])
        permissions_count = sum(1 for meeting_id in meeting_ids if has_perm(meeting_id))
        result.append((committee_name, permissions_count))
    return result