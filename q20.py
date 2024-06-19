
a=input("Enter the string: ")
for i in a:
    if i in [',','.',';','?','!',':',"'",' "',"(",")","/","|","~"]:
        continue
    else:
        print(i, end='')