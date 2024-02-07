import random
from naive_solution import naive_solution
from n_log_n import n_log_n
from arrayLockUpSolution import arrayLockUpSolution
from mapSolution import mapSolution
from factorial_solution import factorial_solution

solutionsFunctions = {
    'Binary Search Solution': n_log_n,
    'Dictionary lookup': mapSolution,
    'Array lookup': arrayLockUpSolution,
    'Factorial solutoion': factorial_solution
}


def stressTesting(threshold):
    for _ in range(threshold):
        n = random.randint(2, 100)
        arr = set([random.randint(2, 100) for _ in range(n+1)])
        arr = list(arr)
        target = random.randint(2, 100)

        correct = naive_solution(arr, target)
        correct.sort()
        for key in solutionsFunctions:
            res = solutionsFunctions[key](arr, target)
            res.sort()
            if res != correct:
                print(f"WRONG ANSWER in {key}")
                print(arr, target, sep='|')
                print(correct, res, sep='|')
                return
    print(f"{threshold} test passed.")

if __name__ == "__main__":
    print("Indique los casos de prueba deseados.")
    t = int(input())
    stressTesting(t)