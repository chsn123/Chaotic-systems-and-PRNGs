m = 2**32
a = 1664525
c = 1013904223
count = 10000
seed = 123456789
import numpy as np

def lcg(count, seed):
    state = seed
    results = []
    for i in range(count):
        state = (a * state + c) % m
        results.append(state / m)
    return results

def logistic(count, seed):
    x = seed / m
    results = []
    for i in range(count):
        x = 4 * x * (1 - x)
        results.append(x)
    return results

def hybrid(count, seed):
    state = seed
    noise = seed / m
    results = []
    for i in range(count):
        # chaotic logistic map
        noise = 4 * noise * (1 - noise)
        # convert logistic value back into an integer
        noise_int = int(noise * m)
        # normal LCG step
        state = (a * state + c) % m
        # mix logistic output into LCG state
        state = state ^ noise_int
        results.append(state / m)
    return results
  
def check(name, values):
    values = np.array(values)
    mean = np.mean(values)
    variance = np.var(values)
    autocorrelation = np.corrcoef(
        values[:-1],
        values[1:]
    )[0, 1]
    bins, _ = np.histogram(values, bins=20, range=(0, 1))
    expected = len(values) / 20
    chi_square = np.sum((bins - expected) ** 2 / expected)
    print(name)
    print("Mean:", mean)
    print("Variance:", variance)
    print("Autocorrelation:", autocorrelation)
    print("Chi-square:", chi_square)
    print()

lcg_values = lcg(count, seed)
logistic_values = logistic(count, seed)
hybrid_values = hybrid(count, seed)
check("LCG", lcg_values)
check("Logistic", logistic_values)
check("Hybrid", hybrid_values)
