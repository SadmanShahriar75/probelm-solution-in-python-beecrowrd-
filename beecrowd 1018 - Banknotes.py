a = int(input())
banknotes = [100, 50, 20, 10, 5, 2, 1]
print(a)
for i in banknotes:
  x = a // i
  a = a % i
  print(f"{x} nota(s) de R$ {i},00")