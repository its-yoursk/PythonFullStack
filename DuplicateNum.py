n=int(input("How many elements?"))
list=[]
for i in range(n):
    element=int(input("Enter element: "))
    list.append(element)
duplicate=[]
count=0
for i in list:
    if list.count(i)>1 and i not in duplicate:
        duplicate.append(i)
        count+=1
        print("Duplicate elements:", duplicate, count)