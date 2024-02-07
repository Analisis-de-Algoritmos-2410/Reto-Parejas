from mapSolution import mapSolution
from naive_solution import naive_solution
from n_log_n import n_log_n
from arrayLockUpSolution import arrayLockUpSolution
from factorial_solution import factorial_solution
from matplotlib import pyplot as plt
import random
import pandas as pd
import time

solutionsFunctions = {
    'Naive Solution': naive_solution,
    'Binary Search Solution': n_log_n,
    'Dictionary lookup': mapSolution,
    'Array lookup': arrayLockUpSolution,
    'Factorial solution': factorial_solution
}

def main():
    t = {
        'Naive Solution': [],
        'Binary Search Solution': [],
        'Dictionary lookup': [],
        'Array lookup': [],
        'Factorial solution': []
    }
    for n in range(1, 100):
        arr = [random.randrange(-100, 100) for _ in range(n+1)]
        arrForArrayLookup = [random.randrange(0, 200) for _ in range(n+1)]
        target = random.randrange(-100, 100)

        for key in solutionsFunctions:
            start = time.perf_counter()
            if key == 'Array lookup':
                solutionsFunctions[key](arrForArrayLookup, target)
            else:
                solutionsFunctions[key](arr, target)
            final = time.perf_counter()
            t[key].append(final-start)
    df = pd.DataFrame(t)
    df.index.name = 'n'
    df.reset_index(inplace=True)
    for key in solutionsFunctions:
        plt.plot(df['n'], df[key], label=key)
    plt.legend()
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.title('Execution times')
    plt.show()



if __name__ == '__main__':
    main()