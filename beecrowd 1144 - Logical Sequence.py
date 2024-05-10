n = int(input())
s = 1
k = 1
for i in range(n):
   print(f"{s} {s**2} {s**3}")
   print(f"{k} {k**2+1} {k**3+1}")
   s = s + 1
   k = k + 1