import math
a, b, c  = map(float,input().split())
formula = b**2 - 4*a*c

if  a == 0 or formula<0:
    print("Impossivel calcular")  
 
else:
    X = (-b + math.sqrt(formula)) / (2*a)
    Y = (-b - math.sqrt(formula))/ (2*a)
    print(f"R1 = {X:.5F}")
    print(f"R2 = {Y:.5F}")

 