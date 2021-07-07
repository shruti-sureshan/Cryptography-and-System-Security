import hashlib 

# initializing string 
str = input("Enter a string:     ")

# then sending to md5() 
result = hashlib.md5(str.encode()) 

# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of hash is : ", end ="") 
print(result.hexdigest()) 
