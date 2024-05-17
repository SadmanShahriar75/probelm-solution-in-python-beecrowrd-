n = int(input())
rs = 0
s = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a ==1001:
        rs = 1.50
    elif a==1002:
        rs = 2.50
    elif a==1003:
        rs = 3.50
    elif a== 1004:
        rs = 4.50
    elif a == 1005:
        rs = 5.50
    total = rs * b
    s+= total
print(f"{s:.2f}")