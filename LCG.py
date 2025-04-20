import matplotlib.pyplot as plt
def lcg(a, c, m, seed, n):
    values = []
    x = seed
    for _ in range(n):
        x = (a * x + c) % m
        values.append(x)
    return values

# Values

a = 5
c = 3 
m = 9
seed = 1
n = 20

# This combo violates the rules of Hull-Dobell's theorem
# Small m chosen to show repetition of LCG

values = lcg(a, c, m, seed, n)
plt.figure(figsize=(8, 3))
plt.plot(values, marker='o', linestyle='-', color='teal')
plt.title("xₙ₊₁ = (5 * xₙ + 3) mod 9")
plt.xlabel("Iteration")
plt.ylabel("Value")
plt.grid(True)
plt.show()
