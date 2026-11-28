# # que 1
# def show(n):
#     if n == 0:
#         print("Stop")
#         return
#     print(n)
#     show(n - 1)
#     print(n)
# show(2)
# output =  2
#           1
#         Stop
#           1
#           2
  
# # que 2
# def total(n):
#     if n == 0:
#         return 0
#     return n + total(n - 1)
# base-case = if n==0:
#              return 0

# # que 3
# def count(n):
#     if n == 0:
#         return
#     count(n + 1)
# bug = we are not calling the function.

# # que 4
# def answer(n):
#     if n == 0:
#         return 0
#     n + answer(n - 1)
# print(answer(3))
# on 36th line return i will write

# # que 5
# def countdown(n):
#     if n ==0:
#         return "Done!"
#     print(n)
#     return countdown(n-1)
# print(countdown(3))

# que 6
# def count_up(n):
#     if n==0:
#         return 
#     count_up(n-1)
#     print(n)
# print(count_up(4))

# # que 7
# addition = 0
# def sum_to(n):
#     if n == 0:
#         return 0
#     return n + sum_to(n - 1)
# print(sum_to(4))

# # que 8
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))

# # que 9
# def digit_sum(n):
#     if n < 10:
#         return n
#     return (n % 10) + digit_sum(n // 10)
# print(digit_sum(583))

# # que 6 second method
# count = 0
# def fun(n,count):   
#     if n == count:
#         return
#     count+=1
#     print(count)
#     fun(n,count)
# fun(4,count)

# # que 10
# def power(base,exponent):
#     if exponent<=0:
#         return 1
#     return base*power(base,exponent-1)
# print(power(2,5))

# # que 11
# def digits_digit(n):
#     if n < 10:
#         return 1
#     return 1 + digits_digit(n//10)
# print(digits_digit(12345))

# # que 12
# def reverse_text(text):
#     if text == "":
#         return ""
#     return reverse_text(text[1:]) + text[0]
# print(reverse_text("cat"))

# # que 13
# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(6))

# # que 14
# def max_digit(n):
#     if n < 10:
#         return n
#     last_digit = n % 10
#     max_rest = max_digit(n // 10)
#     if last_digit > max_rest:
#         return last_digit
#     else:
#         return max_rest
# print(max_digit(4729)) 

# # que 15
# def mystery(n):
#     if n <= 1:
#         return n
#     return mystery(n - 1) + mystery(n - 2)
# print(mystery(4))
# output = 3

# # que 16
# def factorial(n):
#     if n == 0:
#         return 1

#     return n * factorial(n - 1)
# print(factorial(5))

# # que 17
# def stop_at_zero(n):
#     if n == 0:
#         return "zero"

#     return  stop_at_zero(n-1)
# print(stop_at_zero(5))

# 18
#RecursionError error will occur . when we call function too many time it will go deeper and deeper inside a function without
#finishing that outer function and it will take more and more frames inside the functions.