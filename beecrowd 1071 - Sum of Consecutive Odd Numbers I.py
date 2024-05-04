x = int(input())
y = int(input())

total = 0
if x > y:
    x, y = y, x

for i in range(x+1, y):
    if i % 2 == 1:

        total += i

print(total)
