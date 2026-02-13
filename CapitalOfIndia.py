n=int(input("How many elements? "))
    my_dict={}
      for i in range(n):
          key=input("Enter key: ")
          value=input("Enter value: ")
          my_dict[key]=value
      print(my_dict)
      key_to_remove=input("Enter key to remove: ")
      if key_to_remove in my_dict:
          del my_dict[key_to_remove]
          print("Updated Dictionary:",my_dict)
      else:
          print("Key not found in the dictionary.")
