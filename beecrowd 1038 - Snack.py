x, y = map(int,(input().split()))
prices =[0,4.00, 4.50, 5.00, 2.00, 1.50]
pay = prices[x]*y
print(f"Total: R$ {pay:.2f}")
