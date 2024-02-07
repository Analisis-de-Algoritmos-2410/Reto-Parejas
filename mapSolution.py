from collections import defaultdict

def mapSolution(arr, target):
    lockup = defaultdict(lambda: 0)
    ans = []
    for item in arr:
        if lockup[item] > 0:
            ans.append((item, target-item))
        else:
            lockup[target-item] += 1
    return ans