import numpy as np
import matplotlib.pyplot as plt

r = 4 #Growth rate
iterations = 50
pop1 = 0.59
pop2 = 0.6

def logistic_map(r, x):
    return r * x * (1 - x)

plot1 = [pop1]
plot2 = [pop2]
for _ in range(iterations - 1):
    plot1.append(logistic_map(r, plot1[-1]))
    plot2.append(logistic_map(r, plot2[-1]))
    
plt.figure(figsize=(10, 6))
plt.plot(plot1, label='Initial population = 0.59', linewidth=2)
plt.plot(plot2, label='Initial population = 0.6', linewidth=2)
plt.title('Sensitivity to initial conditions in logistic map with r = 4')
plt.xlabel('Iteration')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
