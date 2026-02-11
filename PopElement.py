n=int(input("How many elements? "))
my_sets=set()
for i in range(n):
    element=input("Enter element: ")
    my_sets.add(element)
print(my_sets)
element_to_remove=input("Enter element to remove: ")
if element_to_remove in my_sets:
    my_sets.pop()
    print("Updated Sets:",my_sets)
else:
    print("Element not found in the set.")
