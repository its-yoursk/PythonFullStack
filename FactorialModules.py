import math
num=int(input("Enter a number: "))
if num<0:
    print("The number is negative. Factorial is not defined for negative numbers.")
elif num==0:
    print("The factorial of 0 is 1.")
else:   
    factorial=math.factorial(num)
    print("The factorial of", num, "is", factorial)
    