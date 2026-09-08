#1

a=10
if a>10:
    print("a is greater than 10")

#2
age=20
if age>=18:
    print("You are eligible to vote")

#3
b=int(input("Enter your number:"))
if b > 0:
    print("You have entered a positive number")

#4
c=int(input("Enter your marks:"))
if c >= 40:
    print("You have passed the exam")
else:
    print("You have failed the exam")

#5
d=int(input("Enter your number:"))
if d == 0:
    print("You have entered zero")

#6
e=int(input("Enter your number:"))
if e > 0:
    print("You have entered a positive number")
else:
    print("You have entered a negative number")

#7
age1=int(input("Enter your age:"))
if age1 >= 18:
    print("adult")
else:
    print("minor")

#8
a1=int(input("Enter a number: "))
if a1 % 2 == 0:
    print("your number is Even")
else:
    print("your number is Odd")

#9
marks1=int(input("Enter your marks: "))
if marks1 >= 40:
    print("You have passed the exam")
else:
    print("You have failed the exam")

#11
marks2=int(input("Enter your marks: "))
if marks2 >= 90:
    print("You have got A grade")   
elif marks2 >=75:
        print("You have got b grade")  
elif marks2 >=60:
        print("You have got c grade") 
elif marks2 >=40:
        print("You have got d grade")
else:
    print("you are fail in exam")  

#12

num=input("input your number")
if num > 0:
    print("your number is positive")
elif num == 0:
    print("your number is zero")
else:
    print("your number is negetive")

#13

num1=input("choose your number(1,2,3,4,5)")
if num1 == 1:
    print("you choose monday")
elif num1 == 2:
    print("you choose tuesday")
elif num1 == 3:
    print("you choose wedneaday")
elif num1 == 4:
    print("you choose thursday")
elif num1 == 5:
    print("you choose friay")

#14

marks3=input("enter your marks")

if marks3 > 90:
    print("excellent")
elif marks3 > 75:
    print("good")
elif marks3 > 33:
    print("pass")
else:
    print("fail")

#15

num2=input("input your number")
if num2 == 1:
   print("number is 1")
elif num2 == 2:
    print("number is 2")
elif num2 == 3:
    print("number is 3")
else:
    print("other")

#16

a2 = int(input("Enter the age: "))
if a2 >= 18:
    if a2 <= 60:
        print("Between 18 and 60")


#17

marks4=input("your marks")
if marks4 >= 40:
    print("PASS")
elif marks >= 75:
    print("good")
else:
    print("failed")

18

num=int(input("enter a number: "))
if num>=0:
    if num>=100:
     print("number is greater than 100 and positive")
else:
   print("number is not grater than 100 and positive")

19

age=int(input("enter your age: "))
if age>=18 and age<=60:
   print("you can vote")
else:
   print("you cannot vote")

20

a=int(input("enter number: "))
if a!=0:
   if a>=0:
      print("number is positive")
   if a<=0:
      print("number is negative")

21

age=int(input("inter your age: "))
marks=int(input("inter your marks: "))
if age>=18 and marks>=40:
    print("you are eligible for college")
else:
    print("you are not eligible")

22

num=int(input("enter a number: "))
if num<10 or num>100:
    print("special")
else:
    print("not special")

23

age=int(input("enter age: "))
has_id=True
if age>=18 and has_id ==True:
    print("allowed")
else:
    print("not allowed")

24

first_num=int(input("enter 1 num: "))
second_num=int(input("enter 2 num: "))
if first_num>10 and second_num>10:
    print("both are greter than 10")

25

a=int(input("take a number: "))
if a<0 or a>100:
    print("true")

26

is_closed= False
if not is_closed:
    print("opened")

#27
a=int(input("enter num"))
if a>10 and a<50:
    print("a is between 10 and 50")

#28
num =int(input("enter number"))
if num>10 or num<50:
    print("it is outsideof rang")

#29

is_student= True
has_id=True
has_ticket=True
if is_student and has_id and has_ticket==True
   print("allowed")

#30
age=int(input("age"))
marks=int(input("marks"))
has_id = True
if age >= 18 and marks >= 40 and has_id is True:
    print("eligable")
else:
    print("not eligable")