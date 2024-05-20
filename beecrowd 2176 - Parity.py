n = input()
s = 0
for m in n:
    if m == "1":
        s = s +1
if s % 2 == 0:
    n = n + "0"
else:
    n = n + "1"
print(n)