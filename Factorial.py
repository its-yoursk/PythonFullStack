num=int(input("Enter a number: "))
for i in range(1,num+1):
    factorial=1
    for j in range(1,i+1):
        factorial *= j
print("Factorial of",i,"is",factorial)