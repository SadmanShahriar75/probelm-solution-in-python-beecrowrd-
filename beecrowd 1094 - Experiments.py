n = int(input())
C= 0
R = 0
S = 0
for i in range(n):
  a, ch = map(str, input().split())
  a = int(a)
  if ch == "C":
     C=C+a
  if ch == "R":
     R=R+a
  if ch == "S":
    S = S+a
total = C+R+S
x = (C*100)/total
y = (R*100)/total
z = (S*100)/total

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {C}")
print(f"Total de ratos: {R}")
print(f"Total de sapos: {S}")
print(f"Percentual de coelhos: {x:.2f} %")
print(f"Percentual de ratos: {y:.2f} %")
print(f"Percentual de sapos: {z:.2f} %")