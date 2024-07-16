import random

computer = random.choice(["s","sc","p"])
# print(computer)

you = input("Enter your choise: ")
print(f"Computer chooses: {computer}\n You chooses: {you}")

if(computer==you):
    print("Draw")

else:
    
    if(computer=="s" and you == "sc"):
        print("Computer won!")
    elif(computer=="s" and you == "p"):
        print("You won!")
    elif(computer=="sc" and you == "s"):
        print("You won!")
    elif(computer=="sc" and you == "p"):
        print("Computer won!")
    elif(computer=="p" and you == "s"):
        print("computer won!")
    elif(computer=="p" and you == "sc"):
        print("You won!")

    else:
        print("Something is wrong")