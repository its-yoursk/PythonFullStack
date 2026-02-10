n = int(input("How many elements? "))
list=[]
for i in range(n):          
    element=int(input("Enter element: "))
    list.append(element)
print(list[0])
print(list[-1] )
print(len(list) )