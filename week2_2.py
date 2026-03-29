= float(input("Enter principal amount: "))
r = float(input("Enter annual interest rate (in %): ")) / 100
t = float(input("Enter time (in years): "))
n = int(input("Enter number of times interest is compounded per year: "))
a = p * (1 + r/n) ** (n * t)
ci = a - p
print(f"\nFinal Amount: {a}")
print(f"Compound Interest: {ci}")


