def arrayLockUpSolution(lst, target):
  max_num = max(lst)
  cnt = [0] * (max_num + 1)

  for n in lst:
      cnt[n] += 1

  pairs_set = set()

  for n in lst:
      complemento = target - n
      if complemento >= 0 and cnt[complemento] > 0:
          pair = (min(n, complemento), max(n, complemento))
          pairs_set.add(pair)
          cnt[complemento] -= 1

  return list(pairs_set)

lst = [1, 9, 5, 0, 20, -4, 12, 16, 7]
target = 12
print(arrayLockUpSolution(lst, target))
