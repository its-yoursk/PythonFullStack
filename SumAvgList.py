n=int(input("How many elements? "))
lst=[]
for i in range(n):
    element=int(input("Enter element: "))
    lst.append(element)
    total=sum(lst)
    average=total/n 
print("Sum:", total)
print("Average:", average)
