n=int(input("Enter the first number: "))
lst=[]
for i in range(n):
    num=float(input("Enter a number: "))
    lst.append(num)
def MaxNum(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val
result = MaxNum(lst)
print(f"The maximum number in the list is: {result}")
