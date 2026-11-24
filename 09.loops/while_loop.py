# # table of 2
# i = 1
# while i <=10:
#     print(i*2)
#     i+=1

# # decreasing order
# i = 10
# while i>=0:
#     print(i)
#     i-=1

# partten question
# i = 1
# while i<=3:
#     j = 1
#     while j<=3:
#         print("*",end="")
#         j+=1
#     print()
#     i+=1

# # password 
# x = int(input("enter your password: "))
# while x!=12345:
#     print("you entered wrong password:")
#     x = int(input("enter your password again: "))
# print("your password is correct!!!")

# # palindrome 
# str = input("enter a string: ")
# i = 0
# j = len(str)-1
# flag = True
# while i<j:
#     if str[i]==str[j]:
#         i+=1
#         j-=1
#         print("palindrome!!!")
#     else:
#          flag = False
#          i=j   # To break a loop.
#          print("not palindrome!!!")

# # Number processing & while loop
# number = int(input("enter a number: "))

# while number > 0:
#     digit = number % 10
#     print(digit)
#     number = number // 10


# # total of numbers in string
# number = int(input("enter a number: "))
# total = 0

# while number>0:
#     digit = number%10
#     total = total+digit
#     number = number//10
# print("sum:", total)

# # reverse number printing
# number = int(input("Enter a number: "))

# reverse = ""

# while number > 0:
#     digit = number % 10
#     reverse = reverse *0 + digit
#     number = number // 10

# print("Reverse:", reverse)

# # Number patterns
# number = int(input("enter number: "))
# row = 1

# while row <=number:
#     columm = 1
#     while columm <=row:
#         print(columm , end="")
#         columm+=1
#     print()
#     row+=1

