import math
def gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1
num1 = 36
num2 = 60
result = gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is:", result)
