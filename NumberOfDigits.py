num=int(input("Enter a number: "))
count=0
while num>0:
    num=num//10
    count+=1    
# print("The number of digits is:", count)
if(count==1):
    print("The number is a single-digit number.")
elif(count==2):
    print("The number is a two-digit number.")  
elif(count>2):
    print("The number is more than two-digit number.")