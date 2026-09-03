a=" Hello python"

print("Hello" in a)
print("world" not in a)
print(a.find("Hello"))
print(a.index("Hello"))
print(a.startswith("Hello"))
print(a.endswith("python"))

b= "i like java"
c= b.replace("java","python")
print(b)
print(c)

c= "Hello Python  "
d= "Hello Python"
print(c.strip().upper()==d.upper())

path = r"C:\view\soul"
print(path)

name = "dhyani"
age = "19"
status = "student"
print(f"my name is {name} and my age is {age} and i am a {status}")

x = " python-is-difficult"
print(type(x.split("-")))