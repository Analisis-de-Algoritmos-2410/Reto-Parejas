
def arrayLockUpSolution(list, target):
  pairs = []
  cnt = {}

  for n in list:
      complemento = target - n
      if cnt.get(complemento, 0) > 0:
          pairs.append((min(complemento, n), max(complemento, n)))
      else:
          cnt[n] = cnt.get(n, 0) + 1

  return pairs