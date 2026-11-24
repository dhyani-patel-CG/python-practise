# que 1
# for i in range(1, 8):
#     if i == 5:
#         break
#     print(i)
# print("Finished")
# output = 1
# 2
# 3
# 4
# Finished

# que 2
# word = "skyline"

# for ch in word:
#     if ch in "aeiou":
#         break
#     print(ch)
# output = s
# k
# y
# l

# que 3
# n = 2

# while n <= 10:
#     print(n)
#     if n == 6:
#         break
#     n += 2
# output = 2
# 4
# 6

# #que 4
# limit = int(input("enter the limit"))
# for limit in range(1,limit+1):
#     if limit == 7:
#         break
#     print(limit)

# #6
# numbers = [10,-5,-4,-3,2,20,30]
# for numbers in numbers:
#     if numbers<0:
#         continue
#     print(numbers)

# #7
# for row in range(1, 4):
#     for col in range(1, 5):
#         if col == 3:
#             break
#         print(row, col)

#8
# str = input("enter a str:")
# target = input("enter a target:")
# for str in target:
#     if str == target:
#      continue
#     print("found") 
        
# else:
#     print("not found")

#9
# for i in range(1, 7):
#     if i == 4:
#         continue
#     print(i)

#10
# for ch in "education":
#     if ch in "aeiou":
#         continue
#     print(ch, end="")

#11
# n = 0

# while n < 5:
#     n += 1
#     if n == 3:
#         continue
#     print(n)

# #12
# num = int(input("enter a num:"))
# for num in range(1,num):
#     if num %3==0:
#         continue
#     print(num)

#13
# str = input("enter a str:")
# char = input("enter a char:")
# for  str in char:
#     if str == char:
#         continue
#     print("char")


#14
# input_marks = input("enter a marks:").split()

# for marks in input_marks:
#     num = int(marks)
#     if marks<40:
#         print(marks)


# # 15
# for i in range(1, 5):
#     if i == 2:
#         continue
#     print("A", i)
#     print("B", i)

# 16
# n = 0

# while n <= 5:
#     if n == 3:
#         n += 1
#         continue

#     print(n)
#     n += 1

# # 17
# word = input("enter your string: ")
# vowels = "aeiouAEIOU"
# non_vowel_count = 0

# for char in word:
#   if char in vowels:
#     continue 
#   non_vowel_count += 1

# print(f"Word: {word}")
# print(f"Number of non-vowels: {non_vowel_count}")

# # 18
# for i in range(1, 4):
#     print(i)
# else:
#     print("Done")
# output = 1
# 2
# 3
# Done

# # 19
# for i in range(1, 5):
#     if i == 2:
#         continue
#     print(i)
# else:
#     print("Completed")
# # output 1
# 3
# 4
# Completed

# # 20
# for i in range(1, 5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("Completed")
# print("Outside loop")
# output 1
# 2
# Outside loop

# # 21
# for item in []:
#     print("Inside")
# else:
#     print("Else block")
# output = Else block

# # 22
# list = [1,0,3,4,5]
# for ch in range(1):
#      if ch==0:
#         print("found")
#      else:
#        print("not found")

# # 23
# string = input("enter your string: ")
# for i in string:
#     if i=="d":
#         print("character exists")
#         break
# else:
#     print("character missing")

# # 24
# n = int(input("Enter a positive integer greater than 1: "))

# for i in range(2, n):
#     if n % i == 0:
#         print("Not prime")
#         break
# else:
#     print("Prime")

# # 25
# values = [2, 4, 6, 8]

# for value in values:
#     if value % 2 != 0:
#         print("Odd found")
#         break
# else:
#     print("All are even")
# output All are even

# # 26
# # case - A
# for x in range(3):
#     continue
# else:
#     print("A")
# output A

# # case B
# for x in range(3):
#     break
# else:
#     print("B")
# output 

# # case c
# for x in range(0):
#     print(x)
# else:
#     print("C")
# output C

# # 27
# text = "abcded"
# for i in range(len(text)):
#     ch = text[i]
#     if text.find(ch, i + 1) != -1:
#         print(ch)
#         break
# else:
#     print("No repeated character")

# # 28
# for i in range(1, 4):
#     if i == 2:
#         pass
#     print(i)
# output 1
# 2
# 3

# # 29
# x = 10

# if x > 5:
#     pass

# print("Finished")
# output Finished

# # 30
# for letter in "cat":
#     pass

# print("Loop ended")
# output Loop ended

# # 31
# for i in range(1, 6):
#     if i % 2 == 0:
#         pass
#     print(i)

# # 32
# print("--- MENU ---")
# print("1. Say Hello")
# print("2. [Under Construction / Coming Soon]")
# print("9. Exit / Unknown")
# choice = input("Enter your choice: ")
# if choice == "1":
#     print("Hello! Welcome to the program.")
# elif choice == "2":
#     pass 
# elif choice == "9":
#     print("Exiting the menu.")
# else:
#     print("Invalid option selected.")
# print("Program closed")

# # 33
# # program A
# for i in range(1, 5):
#     if i == 3:
#         pass
#     print(i)
# output 1
# 2
# 3
# 4

# # program B
# for i in range(1, 5):
#     if i == 3:
#         continue
#     print(i)
# output 1
# 2
# 4

# # 34
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

# # 35
# for i in range(1, 6):
#     if i == 2:
#         continue
#     if i == 4:
#         break
#     print(i)
# else:
#     print("Finished")
# output 1
# 3

# # 36
# numbers = [-2, 4, 7, 9]
# target = 7
# for num in numbers:
#     if num < 0:
#         continue
    
#     if num == target:
#         print("Target found")
#         break
# else:
#     print("Target not found")
# output Target found

# # 37
# numbers = [2, 0, 4, -1, 8]
# for num in numbers:
#     if num == 0:
#         continue
#     if num == -1:
#         break
        
#     print(num)
# else:
#     print("All values processed")

# # 38
# for row in range(1, 4):
#     for col in range(1, 4):
#         if col == 2:
#             continue
#         if row == 3:
#             break
#         print(row, col)
#     else:
#         print("Inner loop completed")
# #output  1 1
# 1 3
# Inner loop completed
# 2 1
# 2 3
# Inner loop completed

# # 39
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

# 40
# username = input("enter your username: ")
# conform_username = input("enter your username: ")
# for ch in username:
#     if username==conform_username:
#         print(username)
#         break
