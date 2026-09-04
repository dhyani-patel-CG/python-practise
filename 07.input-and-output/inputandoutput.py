# que 1
name=input("enter your name: ")
print("your name is: ",name)

# que 2
city=input("enter your city: ")
print("your city is: ",city)

# que 3 
name=input("enter your name: ")
age=input("enter your age: ")
print(f"your name is {name} and your age is {age}")

# que 4 input () returns string value.

# que 5
a=input("value: ")
print(type(a))

# que 6
first_name=input("enter your first name: ")
last_name=input("enter your last name: ")
print(f"{first_name} {last_name}")

# que 7
name=input("enter your name:")
city=input("enter your city: ")
college=input("enter your college name: ")
print(f"i am {name}, from {city}, studying at {college}.")

# que 8
first_name,last_name=input("enter your first name and last name: ").split()
print(f"{first_name} {last_name}")

# que 9
word1,word2,word3=input("enter 3 words: ").split()
print(word1,word2,word3)

# que 10
word1,word2,word3=input("enter 3 words: ").split()
print(word1,word2,word3)

# que 11
num=int(input("enter a number: "))
print(num)

# que 12
num1=float(input("enter a number: "))
print(num1)

# que 13
num2=100
print(str(num2))

# que 14
num3=str(99)
print(type(num3))

# que 15
num4=int(14.4)
print(num4)

# que 16 & 17
a = input("enter first number: ")
b = input("enter second number: ")

print(int(a) + int(b))

# que 18
name = "Rahul"
age = 20
print(f"my name is {name} and my age is {age}")

# que 19 
a = 10
b = 20
print(f"sum of {a} and {b} is {a+b}")

# que 20
name=input("enter your name: ")
age=input("enter your age: ")
print(f"your name is {name} and your age is {age}")

# que 21
product_price = float(input("enter price: "))
print(f"product price: ${product_price:.2f}")

# que 22 when we have to type only 2 points after decimal we can use :.2f 

# que 23
product_name=input("enter product name: ")
price=float(input("enter price: "))
quantity=int(input("enter quantity: "))
print(f"product name: {product_name} and price: ${price:.2f} and quantity: {quantity} and total price: ${price*quantity:.2f}")

# que 24 print("A", "B", "C") this shows list datatypes

# que 25
print("2026", "08", "19" , sep="-")

# que 26
print("Hello" ,end=" ")
print("world")

# que 27
num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
print(f"sum of {num1} and {num2} is {num1+num2}")

# que 28
Price=float(input("enter price: "))
Quantity=int(input("enter quantity: "))
Total=Price*Quantity
print(f"product price: {Price}and Quantity: {Quantity} and total price: {Total}")

# que 29
name=input("name: ")
age=int(input("age: "))
marks=float(input("marks: "))
print(f"your name is {name}, your age is {age} and your marks are {marks}")

# que 30
student_name=input("enter student name: ")
student_age=int(input("enter student age: "))
student_height=float(input("enter height: "))
city=input("enter city name: ")
print(f"student name: {student_name}and age: {student_age} and height: {student_height:.2f} and city: {city} ")
