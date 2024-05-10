s = 0
p = 0
while True:
    n =  int(input())
    if n < 0:
        break
    s = n + s
    p = p + 1

if p>0:
    total = s / p
    print(f"{total:.2f}")



