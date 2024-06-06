c1, b1, p1 = map(int, input().split())
c2, b2, p2= map(int, input().split())
s= 0
if c2>c1:
  s=s+(c2-c1)
if b2>b1:
  s=s+(b2-b1)
if p2>p1:
  s=s+(p2-p1)
print(s)