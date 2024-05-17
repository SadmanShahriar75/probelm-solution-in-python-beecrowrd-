# for i in range(10):
#     n = int(input ())
#     if n < 1:
#         n=1
#         print(f"X{[i]} = {n}")

x = []

# Read the array
for i in range(10):
    x.append(int(input()))

# Replace null or negative numbers with 1
for i in range(10):
    if x[i] <= 0:
        x[i] = 1

# Print the array
for i in range(10):
    print(f"X[{i}] = {x[i]}")
