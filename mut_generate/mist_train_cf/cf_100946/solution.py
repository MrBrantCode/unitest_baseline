"""
QUESTION:
courses함수는 3개 이상의 수업을 선택해야 하며, 수업들 간의 선수과목 관계를 고려하여 최소한으로 선택해야 하는 수업의 수와 그 수업들을 반환합니다. courses함수는 courses라는 dictionary를 입력으로 받습니다. 이 dictionary의 key는 각 수업을 나타내며, value는 list형태로 해당 수업을 듣기 위한 선수과목의 목록을 나타냅니다. 예를 들어, {1: [], 2: [1], 3: [2], 4: [], 5: [3]}은 수업 1, 2, 3, 4, 5가 있으며, 수업 2는 1을 선수과목으로, 수업 3은 2를 선수과목으로, 수업 5는 3을 선수과목으로 요구한다는 것을 의미합니다. 

courses함수는 각 수업에 대한 정보가 주어졌을 때, 수강해야 할 최소 수업 수와 그 수업들을 반환합니다.
"""

import itertools

def entrance(courses):
    min_length = float('inf')
    result = None
    for comb in itertools.combinations(courses.keys(), 3):
        valid = True
        for course, prerequisites in courses.items():
            if course in comb and not all(p in comb for p in prerequisites):
                valid = False
                break
        if valid and len(comb) < min_length:
            min_length = len(comb)
            result = comb
    return min_length, result