n  = int(input())
N = []
for i in range(1000):
    N.append(i % n)
    print(f"N[{i}] = {N[i]}")