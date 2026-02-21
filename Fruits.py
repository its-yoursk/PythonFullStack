n=int(input("How many elements?"))
fruits=[]
for i in range(n):
    fruit=input("Enter fruit name: ")
    fruits.append(fruit)

fruits.insert(2, "Mango")