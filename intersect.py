n=int(input("How many elements? "))
my_sets1=set()
for i in range(n):
    element=input("Enter element: ")
    my_sets1.add(element)
print(my_sets1)
n=int(input("How many elements? "))
my_sets=set()
for i in range(n):
    element=input("Enter element: ")
    my_sets.add(element)
print(my_sets)
intersection_set=my_sets1.intersection(my_sets)
print("Intersection of two sets:",intersection_set)