ages = list(map(int, input().split()))
H, Z, L = ages
sorted_ages = sorted(ages)
middle_ages = sorted_ages[1]
if middle_ages == H:
  print("huguinho")
elif middle_ages == Z:
  print("zezinho")
elif middle_ages == L:
  print("luisinho")