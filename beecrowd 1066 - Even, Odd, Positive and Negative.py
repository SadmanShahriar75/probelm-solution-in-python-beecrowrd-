s = 0
p = 0
o = 0
r = 0

for i in range(5):
    m  = int(input())
    if m%2 == 0:
        s+=1
    elif m%2 == 1:
         p+=1
    if m>0:
         o+=1
    elif m<0:
          r+=1
     
print(f"{s} valor(es) par(es)")
print(f"{p} valor(es) impar(es)")
print(f"{o} valor(es) positivo(s)")
print(f"{r} valor(es) negativo(s)")

