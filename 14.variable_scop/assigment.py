# # que 1
# def fun():
#     city = "Gujarat"
#     print(city)
#fun()

# # que 2
# school = "codinggita"
# def fun():
#     print()
# fun()

# # que 3
# if True:
#     b = 30
# print(b)

# # que 4
# for i in range(3):
#     pass

# print(i)

# que 5
# scope means where variable name can we access.
# lifetime means for how long time we can access that variable  .

# # que 6
# value = 100
# def test():
#     value = 200
#     print(value)
# test()
# print(value)
# output = 200
#          100

# # que 7
# clicks = 0
# def click():
#     global clicks
#     clicks += 1

# # que 8
# name = "Asha"
# def show():
#     print(name)
#     name = "Ravi"
# show()
# reason => first our code will load then it declare name variable value is Asha .then it will go on invocataion then it call our function then 
# already our function will know that inside function we have variable name but it don't know the value of that variable so on that that after function
# calling it go to function first print line comes on that time it know function has variable named name have but it don't know the value of that variable so it gives error.

# # que 9
# def fun():
#     name = 10
#     def innderfun():
#         nonlocal name 
#         name+=2
#         return name
#     return innderfun
# enjoy = fun()
# print(enjoy())

# # que 10
# def num():
#     numbers = [1,2,3,4,5]
#     return numbers

# number = num()

# # que 11
# def make_counter():
#     count = 0
#     def increment():
#         nonlocal count
#         count += 1
#         return count
#     return increment
# counter = make_counter()
# print(counter())
# print(counter())
# print(counter())

# # que 12
# x = 1
# def outer():
#     x = 2
#     def inner():
#         x = 3
#         print(x)
#     inner()
#     print(x)
# outer()
# print(x)

# output = 3
#          2
#          1

# que 13



# que 14
# def make_counter():
#     count = 0
#     def increment():
#         nonlocal count
#         count += 1
#         return count
#     return increment
# counter = make_counter()
# print(counter())
#reason => first our code will load then it declare name variable value is Asha .then it will go on invocataion then it call our function then 
# already our function will know that inside function we have variable name but it don't know the value of that variable so on that that after function
# calling it go to function first print line comes on that time it know function has variable named name have but it don't know the value of that variable so it gives error.

# que 15
# because list , str , sum , print etc are key word which is declaired by the python.