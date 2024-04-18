
n = 0  
a = 0  
for i in range(6):
    m = float(input())
    if m > 0:
        n = n + 1
        a = a + m
if n > 0:
    x = a / n
    print(f"{n} valores positivos")
    print("{:.1f}".format(x))
