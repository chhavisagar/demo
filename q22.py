

a=int(input("Enter the number of elements you want in your list:"))
l=[]
for i in range(a):
    k=int(input("Enter the element:"))
    l.append(k)

print("the maximum value in the entered list is:",max(l))
print("the minimum value in the entered list is:",min(l))
print("the list is: ",l)