porcoes = [300, 1500, 600, 1000, 150]
s = 225
for i in range(5):
  n = int(input()) 
  s += n * porcoes[i]
print(s)