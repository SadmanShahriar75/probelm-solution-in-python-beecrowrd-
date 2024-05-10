
while True:
  n = int(input())
  if n == 0:
      break
  s = 0
  
  if n % 2 == 0:
    for i in range(n, n + 10, 2):
      s = s + i
  else:
    for i in range(n+1, n + 11, 2):
      s = s + i
      
  print(s)   