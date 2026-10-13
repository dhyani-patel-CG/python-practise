#str = input("enter your string: ")
# flag = True
# count = 0
# for ch in str:
#     count+=1
#     if ch=="o":
#         flag=False
#         print("found")
#         break
# if flag:
#     print("not found")


# str = input("enter your string: ")
# flag = True
# count = 0
# a = len(str)-1
# for i in range(0,a):
#     count+=1
#     if str[i]=="o":
#         print("found")
#         flag = False
#         break
# if flag:
#     print("not found")

# str = "python" 
# for ch in str: #it gives direct charecters not index number , it is called for in loop
#     if ch=="o":
#         print("found!")
#         break

# for i in range(len(str)): # it gives index number , it is called for range loop
#     if str[i]=="o":
#         print("found!")
#         break

# break #
# for i in range(1,11):
#     if i==6:
#         break
#     print(i)

# num = [10,20,30,40,50]
# for ch in num:
#     if ch==30:
#         break
#     print("found")


# while True:
#     num = int(input("enter a number: "))
#     if num==0:
#         break
#     print(num)
#     num = 0

# for i in range(1,100):
#     if i%17==0:
#         break
#     print(i)


# continue #
# for i in range(1,20):
#     if i%2==0:
#         continue
#     print(i)

# num = [10,-2,30,-5,40,-8]
# for ch in num:
#     if ch<0:
#         continue
#     print(ch)

# for i in range(1,20):
#     if i%3==0:
#         continue
#     print(i)

# numbers = [5, 12, 8, 21, 30, 7]
# for ch in numbers:
#     if ch<10:
#         continue
#     print(ch)

# mixed problems #
#que  - 1 => 1 2
# for i in range(1, 6):
#     if i == 3:
#         break
#     print(i)

#que - 2 => 1 2 4 5
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

# que -3 =>12345
# for i in range(1, 6):
#     if i == 3:
#         pass

#     print(i)

#que - 4 => 12
# i = 1
# while i <= 5:
#     if i == 3:
#         continue

#     print(i)
#     i += 1

# que - 5 => 12
# for i in range(1, 5):
#     if i == 2:
#         pass
#     elif i == 3:
#         continue
#     elif i == 4:
#         break
#     print(i)

# que - 6 => nothing
# for i in range(1, 6):
#      if i == 3:
#          break
# else:
#      print("Done")

# que - 7 => done
# for i in range(1, 6):
#     if i == 3:
#         continue
# else:
#     print("Done")

#  challange que :

# que 1
# while True:
#     num = int(input("enter your number: "))
#     if num>0:
#         print(num)
#     elif num<0:
#         continue
#     elif num==0:
#         break

# que 2
# num = [12 , 5 , -4 , 18 , 0 , 25 , 30]
# for ch in num:
#     if ch < 0:
#         continue
#     if ch == 0:
#         break
#     elif ch > 0:
#         print(ch)

# que 3
# list = [ 2, 6 ,  0 , 1 , 4 , 9 , 8 ]
# for ch in list:
#     if ch==1:
#         print("number found")
#     else:
#         print("number not found")

for i in range(1, 5):
    if i == 2:
        pass
    elif i == 3:
        continue
    elif i == 4:
        break
    print(i)
else:
    print("Completed")
print("Outside")