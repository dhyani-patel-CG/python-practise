
#creating a string
name="Dhyani"
city_name='Modasa'
fav_programming_lang="""Python"""
message="hellooo everyone"
print(name)
print(city_name)
print(fav_programming_lang)
print(message)
#empty string
a=""
print(a)
print(len(a))
print(type(a))

#string information
a="Python Programming"
print(a[:])
print(len(a))
print(a[0])
print(a[-1])
print(a[2])
print(a[-2])
#positive indexing
a="Programming"
print(a[0])
print(a[1])
print(a[4])
print(a[-1])
#negative indexing
a="Programming"
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-11])
#indexing challenge
a="Dhyani patel"
print(a[0])
print(a[-1])
print(a[6])
#basic slicing
a="Python Programming"
print(a[0:6])
print(a[7:17])
print(a[:])
print(a[:5])
print(a[-5:])
#slicing with step
a="ABCDEFGHIJKL"
print(a[::2])
print(a[::3])
print(a[1:8:2])
print(a[::-1])
#slicing with negative indexes
a="Python Programming"
print(a[-5:])
print(a[-10:])
print(a[::-1])
#slicing challenge
a="Python Programming"
print(a[:4])
print(a[-3:])
print(a[::2])
print(a[::-1])
print(a[1:-2])
#length
a="hello"
b="hello world"
c="hello how are you all "
print(len(a))
print(len(b))
print(len(c))
#task 12
text = "Python Programming"
print(len(text)-1)
#concatenation
first_name="Dhyani"
last_name="Patel"
print(first_name + ' ' + last_name)
#sentence creation
name="Dhyani"
age=19
age=str(age)
city_name="Modasa"
fav_programming_lang="Python"
print(name + " " + age + " " + city_name + " " + fav_programming_lang)
#string and integer
a=19
a=str(a)
b="age"
print(a+ " " +b)
#string repetation
a="@"
print(a*3)
print(a*5)
print(a*10)
#pattern
a="*" * 10
print(a)


#3

b="Python Programming"

print(b[0:],len(b),b[0],b[18],b[17])

#4

c="Programming"

print(c[0],c[1],c[4],c[9])

#5

print(c[-1],c[-2],c[-3],c[-11])

#6

d="dhyani"

print(d[0],d[5])

#7

print(b[0:6],b[7:],b,b[:5],b[12:])

#8

e="ABCDEFGHIJKL"

print(e[1:8:2])

#9

print(e[1:8:-1])


a="python"

b=a[0:3]
c=a[3:7]
print(b.upper()+c.lower())

#task 18

a = "python programming"
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.swapcase())

#task 19

a="Python"
b="python"
print(a==b)

#10
#task 20

a="python is a programming language"
print("python" in a)
print("programming" in a)
print("java" in a)
print("language" in a)

#task 21

a="python is a programming language"
#task 18 
a="python programming language"
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.swapcase())
#task 19
a="Python"
b="python"
print(a==b)
#task 20
a="Python is a programming language"
print("Python" in a)
print("programming" in a)
print("java" in a)
print("language" in a)
#task 21
a="Python is a programming language"
print(a.find("Python"))
print(a.find("programming"))
print(a.find("java"))
print(a.find("language"))
#task 22
a="Python is a programming language"
print(a.index("Python"))
print(a.index("programming"))
print(a.index("language"))
#task 23
a="banana"
print(a.count("a"))
print(a.count("n"))
print(a.count("b"))
#task 24
filename = "student_notes.pdf"
print(filename.startswith("student"))
print(filename.endswith(".pdf"))
print(filename.endswith(".txt"))
#task 25
text = "I am learning Java"
print(text.replace("Java", "Python"))
#task 26
text = "apple apple apple"
print(text.replace("apple","mango"))
#task 27
text = "apple apple apple"
print(text.replace("apple","mango",1))
#task 28
text = "Python"
text.upper()
print(text)
#task 29
text = "   Python Programming   "
print(text.strip())
print(text.lstrip())
print(text.rstrip())
#task 30
a=input("enter your name:")
print(a.strip())
#task 31
a="Python is easy to learn"
print(a.split())
#task 32
a="apple,banana,mango,orange"
print(a.split(","))
#task 33
words = ["Python", "is", "easy"]
print(" ".join(words))
#task 34
words = ["Python", "is", "easy"]
print("-".join(words))
print("/".join(words))
#task 35
Name="abhay"
age=19
city="mumbai"
print(f"my name is {Name}, I am {age} years old and I live in {city}.")
#task 36
a=10
b=20
print(f"sum of {a} and {b} is {a+b}.")
name = input("Enter your full name: ")
print(name.strip())
print(name)      
print(name.upper())      
print(name.lower())    
print(name.title())       
print(len(name))         
print(name[0])            
print(name[-1])         
print(name.casefold())
#taskt 39
a=input("Enter some text:")
print(a)
print(len(a))
print(len(a.split()))
print(a[0])
print(a[-1])
print(a.upper())
print(a.lower())
print(a.title())
print(a.find("Python"))
print(a.count("a"))
#task 40
first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")
city=input("Enter your city name: ")
course=input("Enter your course name: ")
age=int(input("Enter your age: "))
full_name=first_name + " " + last_name
print(first_name.strip(),last_name.strip(),city.strip(),course.strip(),age)
print(full_name)
print(full_name.upper())
print(full_name.lower())
print(len(full_name))
print(full_name[0])
print(full_name[-1])
print(city,course)
print("Python" in course)
print(course.replace("python","java"))
print(len(course))
