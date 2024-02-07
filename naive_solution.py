def naive_solution(list, target):
    listRetorn = []
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] + list[j] == target:
                listRetorn.append((list[i], list[j]))
    return listRetorn