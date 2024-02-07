import itertools

def factorial_solution(lst, target):
    retorno = set()
    seen = set()
    permutations = list(itertools.permutations(lst, 2))
    for i in permutations:
        if i[0] + i[1] == target:
            if i not in seen and (i[1], i[0]) not in seen:
                retorno.add(i)
                seen.add(i)

    retorno = list(retorno)
    return retorno
