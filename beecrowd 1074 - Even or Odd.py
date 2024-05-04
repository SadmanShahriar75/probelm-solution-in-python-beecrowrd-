a = int(input())
for i in range(a):
  n = int(input())
  if n == 0:
    print("NULL")
  elif  n%2==1 and n<0:
    print("ODD NEGATIVE")
  elif n%2==1 and n>0:
    print("ODD POSITIVE")
  elif n%2==0 and n<0:
    print("EVEN NEGATIVE")
  elif n%2==0 and n>0:
    print("EVEN POSITIVE")

