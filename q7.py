
a=input("Enter a string: ")
count=0
for i in a:
    if(i==" "):
        count+=1
print("the length of the string is:",len(a))
print("The no f words in the string are:",count+1)