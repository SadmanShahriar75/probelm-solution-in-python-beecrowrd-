a, b = map(int, input().split())
if b > a:
    duracao = b - a
else:
    duracao = (24 - a) + b
print(f"O JOGO DUROU {duracao} HORA(S)")

 