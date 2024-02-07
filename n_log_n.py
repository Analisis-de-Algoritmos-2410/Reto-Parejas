def binary_search(inf, sup, list, tar):
  if inf > sup:
    return -1
  else:
    medio = (inf + sup) // 2
    if list[medio] == tar:
      return list[medio]
    elif list[medio] > tar:
      return binary_search(inf, medio - 1, list, tar)
    else:
      return binary_search(medio + 1, sup, list, tar)

def n_log_n(arr, tar):
  ans = []
  arr.sort()
  for i in range(len(arr)//2):
    aj = binary_search(0, len(arr)-1, arr, tar- arr[i])
    if aj != -1:
      ans.append((arr[i], aj))
  return ans
  
