# Part - A #

# # que 1:
# while True:
#     marks = int(input("enter your marks: "))
#     if 0<=marks<=100:
#         print("valid marks")
#         break
#     else:
#         print("invalid marks")

# # que 2:
# while True:
#     num = int(input("enter Integer: "))
#     if num>=0:
#         print("valid positive integer")
#         break
#     else:
#         print("enter again!!!")

# # que 3:
# while True:
#     age = int(input("enter your age: "))
#     if 0<=age<=120:
#         print("your age is:",age)
#         break
#     else:
#         print("Error")

# # que 4:
# while True:
#     print("1.view profile/n2.edit profile/n3.settings/n4.exit")
#     choice = int(input("enter valid choice: "))
#     if choice==1:
#         print("view profile")
#     elif choice==2:
#         print("edit profile")
#     elif choice==3:
#         print("settings")
#     elif choice==4:
#         print("exit")
#         break

# # que 5:
# while True:
#     password = int(input("enter your password: "))
#     if password>=8:
#         print("password is:",password,"successfully applied")
#         break

# # que 6:
# while True:
#     temp = int(input("enter tempreture: "))
#     if -20<=temp<=45:
#         print("temperature",temp)
#         break
#     else:
#         print("invalid tempreture")

# # que 7:
# bank_balance = 5,000
# while True:
#     user = int(input("enter your withdrawal amount: "))
#     if user==0:
#         print(bank_balance)
#         break

# # que 8:
# while True:
#     username = input("Enter a username: ")
#     trimmed_username = username.strip()
#     if len(trimmed_username) >= 5:
#         if " " not in trimmed_username:
#             print(f"Username accepted: {username}")
#             break
#         else:
#             print("Invalid username! The username cannot contain spaces inside.")
#     else:
#         print("Invalid username! It must be at least 5 characters long and cannot be empty.")

# # que 9:
# while True:
#     num = int(input("enter your number: "))
#     if num>0:
#         if num%3==0 and num%5==0:
#             print(num)
#             break

# # que 10:
# pin = 2468
# while True:
#     a = int(input("enter pin: "))
#     if a>=3 and a==pin:
#         print(a)
#         break

# # que 11:
# while True:
#     number = int(input("Enter an integer between 10 and 50: "))
#     if 10 <= number <= 50:
#         print(f"Valid integer accepted: {number}")
#         if number % 2 == 0:
#             print(f"{number} is even.")
#         else:
#             print(f"{number} is odd.")
#         break
#     else:
#         print("Invalid input! Please enter an integer between 10 and 50.")

# # 12.
# balance = 2000
# while True:
#     deposit = int(input("Enter deposit amount: "))
#     if deposit > 0:
#         balance += deposit
#         print("Deposit successful! New balance:", balance)
#         break
#     else:
#         print("Invalid! Deposit must be positive.")

# # 13.
# while True:
#     num = int(input("Enter integer (1-100): "))
#     if 1 <= num <= 100:
#         print("Accepted number:", num)
#         break
#     else:
#         print("Invalid! Must be between 1 and 100.")


# # 14.
# while True:
#     marks = int(input("Enter marks (0-100): "))
#     if 0 <= marks <= 100:
#         if marks >= 75:
#             print("Result: Distinction")
#         elif marks >= 60:
#             print("Result: First Class")
#         elif marks >= 35:
#             print("Result: Pass")
#         else:
#             print("Result: Fail")
#         break
#     else:
#         print("Invalid! Enter between 0 and 100.")


# # 15.
# while True:
#     username = input("Enter username: ").strip()
#     password = input("Enter password: ").strip()
    
#     if len(username) >= 5 and " " not in username and len(password) >= 8 and password != "":
#         print("Login successful!")
#         break
#     else:
#         print("Invalid! Username ≥5 chars, no spaces. Password ≥8 chars.")


# # 16.
# while True:
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#     operator = input("Enter operator (+, -, *, /): ")
    
#     if operator not in ["+", "-", "*", "/"]:
#         print("Invalid operator! Try again.")
#         continue
#     if operator == "/" and num2 == 0:
#         print("Division by zero not allowed! Enter second number again.")
#         continue
    
#     if operator == "+":
#         print("Result:", num1 + num2)
#     elif operator == "-":
#         print("Result:", num1 - num2)
#     elif operator == "*":
#         print("Result:", num1 * num2)
#     elif operator == "/":
#         print("Result:", num1 / num2)
#     break

# # 17.
# balance = 10000
# while True:
#     print("\nBank Menu:")
#     print("1. Check balance")
#     print("2. Deposit money")
#     print("3. Withdraw money")
#     print("4. Exit")
    
#     choice = int(input("Enter choice: "))
    
#     if choice == 1:
#         print("Balance:", balance)
#     elif choice == 2:
#         deposit = int(input("Enter deposit amount: "))
#         if deposit > 0:
#             balance += deposit
#             print("Deposit successful! Balance:", balance)
#         else:
#             print("Invalid deposit!")
#     elif choice == 3:
#         withdraw = int(input("Enter withdrawal amount: "))
#         if withdraw > 0 and withdraw <= balance:
#             balance -= withdraw
#             print("Withdrawal successful! Balance:", balance)
#         else:
#             print("Invalid withdrawal!")
#     elif choice == 4:
#         print("Exiting...")
#         break
#     else:
#         print("Invalid choice! Try again.")


# # 18.
# while True:
#     month = int(input("Enter month (1-12): "))
#     day = int(input("Enter day (1-31): "))
#     if 1 <= month <= 12 and 1 <= day <= 31:
#         print("Accepted date: Month", month, "Day", day)
#         break
#     else:
#         print("Invalid! Month 1-12, Day 1-31.")


# # 19.
# while True:
#     quantity = int(input("Enter product quantity: "))
#     if quantity > 0:
#         break
#     else:
#         print("Invalid! Quantity must be positive.")

# while True:
#     price = float(input("Enter unit price: "))
#     if price > 0:
#         break
#     else:
#         print("Invalid! Price must be greater than 0.")

# print("Total cost:", quantity * price)


# # 20.
# while True:
#     count = int(input("How many numbers (1-20): "))
#     if 1 <= count <= 20:
#         break
#     else:
#         print("Invalid! Must be between 1 and 20.")

# numbers = []
# for i in range(count):
#     while True:
#         num = float(input(f"Enter number {i+1}: "))
#         # Add range check if instructor specifies
#         if True:  # replace with condition if needed
#             numbers.append(num)
#             break
#         else:
#             print("Invalid number! Try again.")

# average = sum(numbers) / count
# print("Average:", average)


# # 21.
# while True:
#     password = input("Enter password: ")
#     errors = []
    
#     if len(password) < 8:
#         errors.append("At least 8 characters")
#     if not any(c.isupper() for c in password):
#         errors.append("At least one uppercase letter")
#     if not any(c.islower() for c in password):
#         errors.append("At least one lowercase letter")
#     if not any(c.isdigit() for c in password):
#         errors.append("At least one digit")
#     if any(c.isspace() for c in password):
#         errors.append("No whitespace allowed")
    
#     if not errors:
#         print("Password accepted!")
#         break
#     else:
#         print("Invalid password! Issues:", ", ".join(errors))

# # 22.
# valid = False
# while not valid:
#     num = int(input("Enter integer (1-10): "))
#     if 1 <= num <= 10:
#         valid = True
#         print("Accepted number:", num)
#     else:
#         print("Invalid! Try again.")


# # 23.
# scores = []
# for i in range(3):
#     while True:
#         score = int(input(f"Enter score {i+1} (0-100): "))
#         if 0 <= score <= 100:
#             scores.append(score)
#             break
#         else:
#             print("Invalid! Must be between 0 and 100.")

# total = sum(scores)
# average = total / 3
# print("Total:", total, "Average:", average)


# # 24.
# balance = 10000
# while True:
#     amount = int(input("Enter withdrawal amount: "))
#     if amount > 0 and amount <= balance and amount % 100 == 0:
#         balance -= amount
#         print("Withdrawn:", amount, "Remaining balance:", balance)
#         break
#     else:
#         print("Invalid! Must be positive, ≤ balance, and multiple of 100.")# 1.
# while True:
#     marks = int(input("Enter marks (0-100): "))
#     if 0 <= marks <= 100:
#         print("Accepted marks:", marks)
#         break
#     else:
#         print("Invalid! Please enter between 0 and 100.")

