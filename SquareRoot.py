num=int(input("Enter a number: "))
if num<0:
    print("The number is negative. Square root is not defined for negative numbers.")
elif num==0:
    print("The square root of 0 is 0.")
else:
    sqrt=num**0.5
    print("The square root of", num, "is", sqrt)