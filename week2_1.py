a = int(input("Enter base: "))
b = int(input("Enter exponent: "))
p = 1
for i in range(b):
    p = p*a
print(f" {a}^{b} is: {p}