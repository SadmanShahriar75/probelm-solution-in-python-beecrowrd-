import math
n = int(input())
n_17 = math.log(n) # 1 step
two_step = n/n_17 # 2 step and lower bound
three_step = two_step * 1.25506
print(f"{two_step:.1f} {three_step:.1f}")




