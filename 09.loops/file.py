str=input("enter a string: ").strip()
str2=""
length=len(str)
for element in range(length-1,-1,-1):
    str2=str2+str[element]
print(str2)


   