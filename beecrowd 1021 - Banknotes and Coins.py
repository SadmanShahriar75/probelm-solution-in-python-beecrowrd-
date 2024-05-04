n = float(input())
notes = [100, 50, 20, 10, 5, 2]
print("NOTAS:")
for i in notes:
  a = n / i
  a_int =int(a)
  n =  float(f"{n%i:.2f}")
  print(f"{a_int} nota(s) de R$ {i}.00")
print("MOEDAS:")
coins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
for i in coins:
  b = n / i 
  b_int =int(b)
  n =  float(f"{n %i:.2f}")
  print(f"{b_int} moeda(s) de R$ {i:.2f}")



    