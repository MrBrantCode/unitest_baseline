"""
QUESTION:
Write a function `addOperators` that takes a string `num` and an integer `target` as input and returns all possible ways to insert the binary operators `+`, `-`, or `*` amidst the digits of `num` such that the resulting expression equals the `target` value. The length of `num` is between 1 and 10 inclusive and `num` only contains digits. The `target` value ranges from `-2^31` to `2^31 - 1`.
"""

def addOperators(num: str, target: int):
    def dfs(pos, prev, multi, cur):
        if pos == len(num):
            if target == prev:
                result.append(cur)
            return
        for i in range(pos, len(num)):
            if num[pos] == '0' and i != pos:  
                break
            curr = int(num[pos: i+1])
            if pos == 0:
                dfs(i+1, curr, curr, cur+str(curr))
            else:
                dfs(i+1, prev+curr, curr, cur+'+'+str(curr))
                dfs(i+1, prev-curr, -curr, cur+'-'+str(curr))
                dfs(i+1, prev-multi+multi*curr, multi*curr, cur+'*'+str(curr))

    result = []
    dfs(0, 0, 0, '')
    return result