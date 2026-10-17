# # 1. 
# def welcome():
#     print("Welcome to Python")

# welcome()
# welcome()
# welcome()


# # 2. 
# def greet(name):
#     print("Hello,", name)

# greet("Rahul")


# # 3. 
# def show_number(number):
#     print(number)

# show_number(10)


# # 4. 
# def add(a, b):
#     return a + b

# print(add(5, 3))


# # 5.
# def square(number):
#     return number * number

# print(square(4))


# # 6. 
# def is_even(number):
#     return number % 2 == 0

# print(is_even(8))
# print(is_even(5))


# # 7. 
# def get_full_name(first_name, last_name):
#     return first_name + " " + last_name

# print(get_full_name("Rahul", "Sharma"))


# # 8. 
# def introduce(name, city="Pune"):
#     print(name, "lives in", city)

# introduce("Rahul")
# introduce("Priya", "Mumbai")


# # 9. 
# def subtract(a, b):
#     return a - b

# print(subtract(10, 3))  # 7
# print(subtract(3, 10))  # -7


# # 10. 
# def get_min_max(a, b):
#     return min(a, b), max(a, b)

# print(get_min_max(12, 5))


# # 11. 
# def calculate(a, b):
#     return a + b, a - b, a * b, a / b

# print(calculate(10, 2))


# # 12. 
# def count_digits(number):
#     return len(str(number))

# print(count_digits(12345))
# print(count_digits(0))


# # 13. 
# def classify_number(number):
#     if number > 0:
#         return "Positive"
#     elif number < 0:
#         return "Negative"
#     else:
#         return "Zero"

# print(classify_number(10))
# print(classify_number(-5))
# print(classify_number(0))


# # 14.
# def calculate_total(price, quantity=1):
#     return price * quantity

# print(calculate_total(50))
# print(calculate_total(50, 3))


# # 15. 
# def create_email(username, domain="example.com"):
#     return username + "@" + domain

# print(create_email("rahul"))
# print(create_email("rahul", "gmail.com"))


# # 16. 
# def format_name(first, last, uppercase=False):
#     name = first + " " + last
#     if uppercase:
#         return name.upper()
#     return name

# print(format_name("Rahul", "Sharma"))
# print(format_name("Rahul", "Sharma", True))


# # 17.
# def percentage(marks, total=100):
#     return (marks / total) * 100

# print(percentage(80))
# print(percentage(45, 50))


# # 18.
# def convert_minutes(minutes, seconds_per_minute=60):
#     return minutes * seconds_per_minute

# print(convert_minutes(5))
# print(convert_minutes(5, 60))


# # 19.
# def student_details(name, age, city):
#     print("Name:", name)
#     print("Age:", age)
#     print("City:", city)

# student_details(city="Pune", name="Rahul", age=18)


# # 20. 
# def bill(item, quantity=1, price=100):
#     return quantity * price

# print(bill("Book"))
# print(bill("Pen", 3, 20))
# print(bill("Bag", price=500, quantity=2))


# # 21.
# def analyze_number(number):
#     absolute_value = -number if number < 0 else number
#     even = number % 2 == 0
#     digits = len(str(absolute_value))
#     return absolute_value, even, digits

# print(analyze_number(-246))


# # 22.
# def calculate_stats(a, b, c):
#     return min(a, b, c), max(a, b, c), a + b + c

# print(calculate_stats(10, 5, 20))


# # 23.
# def make_sentence(subject, verb, object):
#     return subject + " " + verb + " " + object

# print(make_sentence(object="Python", verb="learns", subject="Rahul"))


# # 24.
# def apply_discount(price, discount=0):
#     return price - (price * discount / 100)

# print(apply_discount(1000))
# print(apply_discount(1000, 20))


# # 25.
# def calculate_pay(hours, rate=200, bonus=0):
#     return hours * rate + bonus

# print(calculate_pay(8))
# print(calculate_pay(8, 300))
# print(calculate_pay(8, bonus=500))
# print(calculate_pay(8, rate=300, bonus=500))


# # 26.
# def get_coordinates(x=0, y=0):
#     return x, y

# print(get_coordinates())
# print(get_coordinates(x=5))
# print(get_coordinates(y=10))
# print(get_coordinates(x=5, y=10))


# # 27.
# def compare(a, b):
#     difference = a - b
#     difference = -difference if difference < 0 else difference

#     if a > b:
#         result = "A is greater"
#     elif b > a:
#         result = "B is greater"
#     else:
#         result = "Equal"

#     return result, difference

# print(compare(10, 5))
# print(compare(3, 8))
# print(compare(7, 7))


# # 28. 
# def convert_temperature(value, scale="C"):
#     if scale == "C":
#         return (value * 9 / 5) + 32
#     elif scale == "F":
#         return (value - 32) * 5 / 9

# print(convert_temperature(25))
# print(convert_temperature(98.6, "F"))


# # 29. 
# def calculate_result(marks, passing_marks=35):
#     if marks >= passing_marks:
#         return "Pass"
#     else:
#         return "Fail"

# print(calculate_result(75))
# print(calculate_result(30))
# print(calculate_result(40, 50))


# # 30.
# def order_summary(item, quantity=1, price=100, delivery_fee=40):
#     return quantity * price + delivery_fee

# print(order_summary("Book"))
# print(order_summary("Bag", quantity=2, price=500))
# print(order_summary("Pen", delivery_fee=20))