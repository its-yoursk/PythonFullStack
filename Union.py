n=int(input("How many elements? "))
my_sets1=set()
for i in range(n):
    element=input("Enter element: ")
    my_sets1.add(element)
print(my_sets1)

n=int(input("How many elements? "))
my_sets2=set()
for i in range(n):
    element=input("Enter element: ")
    my_sets2.add(element)
print(my_sets2)
union_set=my_sets1.union(my_sets2)
print("Union of two sets:",union_set)
