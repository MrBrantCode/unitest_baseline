"""
QUESTION:
Alert Names with Frequent Keycard Use

Create a function `alertNames` that takes in three lists: `keyName`, `keyTime`, and `authorizedUses`, and returns a list of unique worker names who received an alert for frequent keycard use in a one-hour period. The returned list should be sorted in ascending order alphabetically. The function should ignore key-card uses marked as 'authorized' in the `authorizedUses` list. 

Restrictions:
- `1 <= keyName.length, keyTime.length, authorizedUses.length <= 10^5`
- `keyName.length == keyTime.length`
- `keyTime[i]` is in the format "HH:MM"
- `[keyName[i], keyTime[i]]` is unique.
- `1 <= keyName[i].length <= 10`
- `keyName[i] contains only lowercase English letters.
- `authorizedUses[i]` is in the format "HH:MM"
"""

def alertNames(keyName, keyTime, authorizedUses):
    data = sorted(zip(keyName, keyTime), key=lambda x: (x[0], x[1])) 
    auth_set = set(authorizedUses)
    res = set()
    i = 0
    while i < len(data):
        if i < len(data) - 2  and data[i][0] == data[i + 2][0]: 
            j = i + 2
            while j < len(data) and data[j][0] == data[i][0]:
                if (int(data[j][1][:2]) * 60 + int(data[j][1][3:]) - int(data[i][1][:2]) * 60 - int(data[i][1][3:]) <= 60) and \
                (data[i][1] not in auth_set and data[j][1] not in auth_set):
                    res.add(data[i][0])
                    break
                j += 1
        i += 1
    return sorted(list(res))