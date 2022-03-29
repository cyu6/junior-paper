import math
import numpy as np
from constants import i, n
"""
Update rule for OPT strategy
- equivalent to the beta = 1 case, where the adversary knows the entire network
- can be considered an upper bound on the rewards gained from this specific attack

Parameters:
D = distribution of expected future rounds won
alpha = proportional stake in system
"""
def opt(D, alpha):
  c = [0]*i # coin values
  r = [0]*i # (expected) reward values
  F = [0]*n # final distribution

  for j in range(n):
    # step 1: draw c1 from exp(alpha)
    c[0] = np.random.exponential(scale=(1/alpha))

    # step 2: calculate ci for all i > 1
    for k in range(1, i):
      c[k] = c[k-1] + np.random.exponential(scale=(1/alpha))

    # step 3: for all i >= 1, draw r_i from D iid
    for k in range(i):
      r[k] = D[np.random.randint(low=0, high=n)]

    # step 4: output sum calculation 
    output_sum = math.exp(-1*(1-alpha)*c[0])
    best_so_far = r[0]
    for k in range(i-1):
      prob = math.exp(-1*(1-alpha)*c[k]) - math.exp(-1*(1-alpha)*c[k+1])
      max_reward = max(best_so_far, r[k])
      output_sum += prob*max_reward

      best_so_far = max_reward

    F[j] = output_sum

  return F
