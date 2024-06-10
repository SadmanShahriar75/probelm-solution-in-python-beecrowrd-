n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    if 200 <= a <= 300 and b >= 50 and c >= 150:
        print("Sim")
    else:
        print("Nao")






