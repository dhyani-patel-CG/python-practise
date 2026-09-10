# a=int(input("enter 3 digit number: "))
# b = a%10
# c = a//10
# d = c%10
# e = c//10
# print(b+d+e)


# print("hello "*100)

# for i in range(1,20):
#     if i%2==0:
#         print(f"{i} is evev!!!" ,end=" ")
#     elif i%2!=0:
#         print(f"{i} is odd!!!" , end=" ")

# sum=0
# for i in range(1,101):
#     total=sum+i
#     avg=total/100
# print(avg)

first_number=int(input("Enter a first number: "))
last_number=int(input("Enter a last number: "))
for i in range(first_number,last_number+1):
    if i%2==0:
        print(f"{i} is even")