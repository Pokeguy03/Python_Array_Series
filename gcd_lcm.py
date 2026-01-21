# Find GCD and LCM of two numbers

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("GCD =", gcd(a, b))
print("LCM =", lcm(a, b))
