n=int(input("How many elements? "))
list=[]
for i in range(n):
    element=(input("Enter element: "))
    list.append(element)

list.remove("Mango")  
list.pop(1)
print(list)