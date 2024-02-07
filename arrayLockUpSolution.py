
def arrayLockUpSolution(list, target):
  pairs = []
  cnt = {}

  for n in list:
      complemento = target - n
      if cnt.get(complemento, 0) > 0:
          pairs.append((complemento, n))
          cnt[complemento] -= 1
      else:
          cnt[n] = cnt.get(n, 0) + 1

  return pairs