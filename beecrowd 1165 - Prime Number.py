n=int(input())
for _ in range(n):
    a=int(input())
    c=0
    for j in range(1, a+1):
        if (a%j==0):
            c+=1
    if (c==2):
        print(f"{a} eh primo")
    else:
        print(f"{a} nao eh primo")
    