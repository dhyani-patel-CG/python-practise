
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