N = int(input())
fibonacci = [0, 1]
print(fibonacci[0], end='')
print('', fibonacci[1], end='')

for i in range(2, N):
    next_number = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(next_number)
    print('', next_number, end='')

print() 