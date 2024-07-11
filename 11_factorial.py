number = int(input("Enter the number: "))

product=1
for i in range(1,number+1):
    product*=i
print(f"Factorial of {number} is {product}")