"""
QUESTION:
In a project, you have a list of required skills req_skills, and a list of people.  The i-th person people[i] contains a list of skills that person has.
Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill.  We can represent these teams by the index of each person: for example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
Return any sufficient team of the smallest possible size, represented by the index of each person.
You may return the answer in any order.  It is guaranteed an answer exists.
 
Example 1:
Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]
Example 2:
Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
Output: [1,2]

 
Constraints:

1 <= req_skills.length <= 16
1 <= people.length <= 60
1 <= people[i].length, req_skills[i].length, people[i][j].length <= 16
Elements of req_skills and people[i] are (respectively) distinct.
req_skills[i][j], people[i][j][k] are lowercase English letters.
Every skill in people[i] is a skill in req_skills.
It is guaranteed a sufficient team exists.
"""

from collections import deque
from typing import List

def find_smallest_sufficient_team(req_skills: List[str], people: List[List[str]]) -> List[int]:
    def fulfill_skills(skills, person):
        remaining_skills = deque()
        for skill in skills:
            if skill not in people[person]:
                remaining_skills.appendleft(skill)
        return remaining_skills
    
    has_skill = dict()
    for person, skills in enumerate(people):
        for skill in skills:
            experts = has_skill.get(skill, [])
            experts.append(person)
            has_skill[skill] = experts
    
    rare_skills = [(len(people), skill) for skill, people in has_skill.items()]
    rare_skills.sort()
    rare_skills = [skill for _, skill in rare_skills]
    
    for i in range(1, 17):
        stack = [(deque(rare_skills), [])]
        while stack:
            skills, team = stack.pop()
            if not skills:
                return team
            if len(team) + 1 > i:
                continue
            skill = skills[0]
            for person in has_skill[skill]:
                remaining_skills = fulfill_skills(skills, person)
                stack.append((remaining_skills, team + [person]))
    
    return []