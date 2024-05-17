t = int(input())
a,b,c,d,e = map(int, input().split())
x = a,b,c,d,e
s=0
for i in x:
    if i == t:
        s = s+1
print(s)
