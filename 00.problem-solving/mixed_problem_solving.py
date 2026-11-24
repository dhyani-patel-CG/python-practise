# #1
# string = input("Enter a string:")
# upper_count = 0
# lower_count = 0
# digit_count = 0
# space_count = 0
# char_count = 0
# for i in string:
#     if i.isupper():
#         upper_count += 1
#     elif i.islower():
#         lower_count += 1
#     elif i.isdigit():
#             digit_count += 1
#     elif i.isspace():
#             space_count += 1
#     else: 
#             char_count += 1
# print("Uppercase:", upper_count)
# print("Lowercase:", lower_count)
# print("Digit:", digit_count)
# print("Space:", space_count)
# print("Character:", char_count)

# if upper_count>digit_count and upper_count>space_count and upper_count>char_count and upper_count>lower_count:
#     print("Highest count is of UpperCase")

# elif lower_count>digit_count and lower_count>space_count and lower_count>char_count and lower_count>upper_count:
#     print("Highest count is of LowerCase")

# elif upper_count<digit_count and digit_count>space_count and digit_count>char_count and digit_count>lower_count:
#     print("Highest count is of Digit")

# elif space_count>digit_count and upper_count<space_count and space_count>char_count and space_count>lower_count:
#     print("Highest count is of Space")

# elif char_count>digit_count and char_count>space_count and char_count>upper_count and char_count>lower_count:
#     print("Highest count is of Special Characters")
# elif upper_count==digit_count or upper_count==space_count or upper_count==lower_count or upper_count==char_count:
#     print("same")