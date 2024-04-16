salary = float(input())
if salary <= 400.00:
    readjustment_rate = 15
elif salary <= 800.00:
    readjustment_rate = 12
elif salary <= 1200.00:
    readjustment_rate = 10
elif salary <= 2000.00:
    readjustment_rate = 7
else:
    readjustment_rate = 4

increase = salary * (readjustment_rate / 100)
new_salary = salary + increase

print("Novo salario: {:.2f}".format(new_salary))
print("Reajuste ganho: {:.2f}".format(increase))
print("Em percentual: {} %".format(readjustment_rate))



