age=int(input("Enter you AGE "))

if(age>=18):
    print("you are allow for voting")
    
elif(age<0):
    print("Please enter a valid age")
    
elif(age==0):
    print("You are not yet born")
else:
    print("You are not allowed")
