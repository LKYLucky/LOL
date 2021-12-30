import random
import math
import numpy as np
import matplotlib.pyplot as plt

# this function calculates the limiting probability
def p(x): 
    t = 2
    lamb = 3.2 
    #poisson distrubution
    p = math.exp(-lamb*t)*((lamb*t)**x)/math.factorial(x)
    return p

n = 10000
x = np.arange(n,dtype=np.float)
# choose a starting point
x[0] = 2
for i in range(n-1):
    # coin flip for symmetric random walk
    flip = random.randrange(2)
    if flip == 1:
        y = abs(x[i] + 1)
    else:
        y = abs(x[i] - 1)
    # uniform samples from [0, 1]    
    U = np.random.random_sample()
    # acceptance probability
    alpha = min(1, p(y)/p(x[i]))
    # accept/reject mechanism
    if U < alpha:
        x[i+1] = y
    else:
        x[i+1] = x[i]
        
# plot N(2) distribution
plt.hist(x, bins = 100)
plt.show() 
# choose N(2) = k
k = x[n-1]
print("number of particles:", int(k))
# k uniformly distributed samples
s = np.random.uniform(0, 2, int(k))
s.sort()
print("arrival times")
for i in range(len(s)):
    print("particle {}: {} seconds".format(i+1, s[i]))

    


