# def f_to_c(f):
#     c=5*(f-32)/9
#     return c

# f = int(input("Enter the Farenheit: "))
# ans = f_to_c(f)
# print(f"{round(ans,2)} °")

def sum(num):
    if(num==1):
        return 1
    return sum(num-1)+num

number = int(input("Enter the number: "))
ans = sum(number)
print(f"{ans}")