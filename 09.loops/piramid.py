# for i in range(1,10,2):
#     for j in range(1,9-i,2):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end="")
#     print()

# a=int(input("enter value: "))
# for i in range(1,a+1,2):
#     for j in range(1,a-i,2):
#         print(" ",end="")
#     for k in range(1,a-i):
#         print("*",end="")
#     print()

# for i in range(5):
#     for j in range(4):
#         print(" ",end="")
#     print("*")
# print(" ")
# for k in range(3):
#       print("*",end="")
# for m in range(5,0,-1):
#       print(" ",end="")
# for n in range(4):
#         print("*")

n = int(input("enter a value: "))
for row in range(1,n+1):
    for col in range(1,n+1):
        if col==1 or col==n or row==n:
            print("*",end="  ")
        else:
            print(end="   ")
        if n%2!=0:
         m=(n+1)/2
         if row==m and col==m:
            print("*")
    print()