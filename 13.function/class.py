# question - 1:
# a = int(input("enter number: "))
# b = int(input("enter number: "))
# def addition():
#     print("addition of two numbers:",a+b)

# def substaction():
#     print("substation of two numbers:",a-b)

# def multiplication():
#     print("multiplication of two numbers:",a*b)

# def floor_division():
#     print("floor division of two numbers:",a//b)

# def even():
#     if a%2==0:
#         print( a, "is even number")
#     if b%2==0:
#         print( b, "is even number")

# def odd():
#     if a%2==1:
#         print(a,"is odd number")
#     if b%2==1:
#         print( b, "is odd number")

# addition()
# substaction()
# multiplication()
# floor_division()
# even()
# odd()

# question - 2:
# def addition(a,b):
#     c = a + b
#     print(c)
# a = int(input("enter a number: "))
# b = int(input("enter a number: "))

# addition(a , b)


# question - 3:
# def double(number):
#     return number * 2

# def add_five(number):
#     return number + 5

# result = add_five(double(10))
# print(result)


# # recurction : 
# def counter_fun(count):
#     count += 1
#     if (count==5):
#         return count
#     return counter_fun(count)
# print(counter_fun(1))

# def info(name="pp" , age=6):
#     print(age)
#     return 5
# b=info(name="dhyani",age=20)
# print (b)
# print(info(name="dhyani",age=20))

###===>>
# def inf(a,c,*args):
#     print(a,b,c)
#     print(args)
# inf("patel",7,6,5,"h",3,2,1,0,"dhyani",b=88)

###===>>
# word = " "
# word1 = "callofduty"
# for word in word1:
#     print("true")
#     break
# else:
#     print("false")


###===>>
# def divide(c,d=15,/,*,a,b=2):
#     return a/b,c+d

# print(divide(15,a=10))


###===>>
# def book_ticket(source, destination, /, *, passenger, seat="regular"):
#     print(source, "to", destination)
#     print("Passenger:", passenger)
#     print("Seat:", seat)

# book_ticket("Pune", "Mumbai", passenger="Asha", seat="window")
# book_ticket("Pune", "Mumbai", passenger="Asha")


###===>>
# def add(*args):
#     print(args)
#     print(type(args))

# add(10, 20, 30)


###===>>>
# def add(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# add(a=10, b=20, c=30)


# text = "callofduty"
# target = "duty"

# found = False

# for i in range(len(text) - len(target) + 1):
#     match = True

#     for j in range(len(target)):
#         if text[i + j] != target[j]:
#             match = False
#             break

#     if match:
#         print("Found:", text[i:i + len(target)])
#         found = True
#         break

# if not found:
#     print("Not found")

# def show_letters(a, b, c):
#     print(a, b, c)

# show_letters(*"cat")  

