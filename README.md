Chaotic Systems and PRNGs

This project compares a chaotic system (logistic map) with a pseudorandom number generator called a linear congruential generator (LCG).

I wanted to see how they differ in things like repetition, sensitivity to starting values and how random their outputs look.

Files

- `LCG.py` - shows how an LCG works and how bad parameters can cause short repeating cycles
- `Logistic_map.py` - shows how very similar starting values can quickly produce very different results
- `Hybrid.py` - combines the logistic map with an LCG and compares the output using some basic statistical tests

Tests used

I compared the generators using:

- mean
- variance
- autocorrelation
- chi-square

The hybrid generator gave results similar to the LCG in the tests I ran, but this does not prove it is better. I still need to test it using more seeds and larger samples.

Libraries

- NumPy
- Matplotlib
