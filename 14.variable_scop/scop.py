# a = input("Enter a number: ")
# length = len(a)
# count = 1
# output = ""
# for i in range(1, length):
#     if a[i] == a[i-1]:
#         count += 1
#     else:
#         output += a[i-1] + str(count)
#         count = 1
# output += a[-1] + str(count)
# print(output)


# def outer():
#     list="hii"
#     def inner():
#         global list
#         print(list("hello"))
#     inner()
# outer()

def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
counter = make_counter()
print(counter())
print(counter())
print(counter())