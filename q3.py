
a=int(input("Enter the number you want to obtain the factorial of:"))
prod=1
for i in range(1,a+1):
    prod*=i
print("The factorial of the given number is:",prod)