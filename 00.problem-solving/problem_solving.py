# level 1
# 1
number=int(input("enter a number: "))
if number>0:
    print("number is positive")
elif number<0:
    print("number is negative")
elif number==0:
    print("number is 0")

# 2
num=int(input("enter number: "))
if num>0 and num%2==0:
    print("positive even")
elif num<0 and num%2==0:
    print("negative even")
elif num>0 and num%2!=0:
    print("positive odd")
elif num<0 and num%2!=0:
    print("negative odd")
elif num==0:
    print("zero")

# 3
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
if num1>num2:
    print(num1)
elif num1<num2:
    print(num2)
elif num1==num2:
    print("both are same number")

# 4
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
num3=int(input("enter third number: "))
if num1>num2 and num3>num2:
    print(num2)
elif num2>num1 and num3>num1:
    print(num1)
elif num1>num3 and num2>num3:
    print(num3)
elif num1==num2==num3:
    print("all are same numbers")
elif num1>num2 and num2==num3:
    print(f"num2 and num3 are same and smallest:{num2}")
elif num2>num1 and num1==num3:
    print(f"num1 and num3 are same and smallest:{num1}")
elif num3>num2 and num2==num1:
    print(f"num1 and num2 are same and smallest:{num2}")
elif num1>num2 and num1==num3:
    print(num2)
elif num3>num1 and num2==num3:
    print(num1)
elif num2>num3 and num2==num1:
    print(num3)

#5
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
num3=int(input("enter third number: "))
if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
elif num3>num1 and num3>num2:
    print(num3)
elif num1==num2==num3:
    print("all are same numbers")
elif num1>num2 and num2==num3:
    print(f"num2 and num3 are same and biggest{num1}")
elif num2>num1 and num1==num3:
    print(f"num1 and num3 are same and biggest{num2}")
elif num3>num2 and num2==num1:
    print(f"num1 and num2 are same and biggest{num3}")
elif num1>num2 and num1==num3:
    print(num1)
elif num3>num1 and num2==num3:
    print(num3)
elif num2>num3 and num2==num1:
    print(num2)

#6
num=int(input("enter a number: "))
if num%5==0 and num%11 ==0:
    print("divisible by 5 and 11")
elif num%5==0:
    print("divisible by 5")
elif num%11==0:
    print("divisible by 11")
else:
    print("divible by neither")

#7
num=int(input("enter a number: "))
if num%3==0 and num%7 ==0:
    print("divisible by 3 and 7")
elif num%3==0:
    print("divisible by 3")
elif num%7==0:
    print("divisible by 7")
else:
    print("divible by neither")

#8
marks=int(input("enter your marks: "))
if marks>100:
    print("Invalid marks")
elif marks<0:
    print("Invalid marks")
elif marks>=40:
    print("pass")
elif marks<40:
    print("fail")

#9
marks=int(input("enter your marks:"))
if marks>=90 and marks<=100:
    print("A")
elif marks>=80 and marks<=89:
    print("B")
elif marks>=70 and marks<=79:
    print("C")
elif marks>=60 and marks<=69:
    print("D")
elif marks>=40 and marks<=59:
    print("E")
elif marks<40:
    print("Fail")

#10 
age=int(input("enter your age: "))
if age<=0:
    print("Invalid age")
elif age<18:
    print("cannot vote")
elif age>=18:
    print("can vote")

level 2

11
year=int(input("enter year: "))
if year%4==0:
    print("This year is a leap year")
else:
    print("This year is not a leap year")

#12
cha=input("enter value: ")
if "A"<=cha<="Z":
    print("uppercase alphabate")
elif "a"<=cha<="z":
    print("lowercase alphabate")
elif 0 <= int(cha) <= 9:
    print("digit")
elif 33<ch<126:
    print("special charecters")

#13
a=input("enter value: ").lower()[:1]
if a=="a"or a=="e"or a=="i"or a=="o"or a=="u":
    print("Vowels")
elif a!="a"or a!="e"or a!="i"or a!="o"or a!="u":
    print("consonant")
else:
    print("Invalid")

#14
cost_price=int(input("cost price: "))
selling_price=int(input("selling price: "))
if selling_price-cost_price>0:
    print("profit")
elif selling_price-cost_price<0:
    print("Loss")
elif selling_price-cost_price==0:
    print("no profit and no loss")

#15
cost_price=int(input("cost price: "))
selling_price=int(input("selling price: "))
profit=(selling_price-cost_price>0)/cost_price*100
loss=(selling_price-cost_price<0)/cost_price*100
if selling_price>cost_price:
    print(f"profit is {profit} ")
elif selling_price<cost_price:
    print(f"loss is {loss} ")
elif selling_price-cost_price==0:
    print("no profit and no loss")

#16
unit=int(input("enter units: "))
if unit <= 100:
    bill = unit*5
elif unit <= 200:
    bill = (100*5) + (unit - 100)*7
else:
    bill = (100*5)+(100*7)+(unit-200)*10

print("bill is",bill)

#17
first_number=int(input("enter first number: "))
second_number=int(input("enter second number: "))
print("1.addition,2.substation,3.multiplication,4.division")
opration=input("enter opration which do you want to do:")
if opration==1:
    print(first_number+second_number)
elif opration==2:
    print(first_number-second_number)
elif opration==3:
    print(first_number*second_number)
elif opration==4:
    print(first_number/second_number)

#18
temp=int(input("enter tempreture: "))
if temp<0:
    print("Freezing")
elif 0<=temp<=15:
    print("Very cold")
elif 16<=temp<=25:
    print("Cold")
elif 26<=temp<=35:
    print("Normal")
elif temp>35:
    print("Hot")

#19
a=int(input("enter number: "))
if a<0:
    print("Negative")
elif 0<=a<=10:
    print("0-10")
elif 11<=a<=50:
    print("11-50")
elif 51<=a<=100:
    print("51-100")
elif a>100:
    print("above 100")

level 3
#20
a=int(input("enter first triangle lenths: "))
b=int(input("enter second triangle lenths: "))
c=int(input("enter third triangle lengths: "))
if a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Invalid triagle")

#21

a=int(input("input value of first side"))
b=int(input("input value of secound side"))
c=int(input("inpyt value of third side"))
if a == b == c:
    print("Equilateral")
elif a == b != c:
    print("Isosceles")
elif a != b == c:
    print("Isosceles")
elif a != b != c:
    print("Scalene")

#22

acoutbal=int(input("enter balance of your account"))
withdrawal_amount=int(input("enter withdrwal amount"))
if withdrawal_amount <= 0:
        if withdrawal_amount % 100 != 0:
              if withdrawal_amount > acoutbal:
                 if (acoutbal - withdrawal_amount) < 500:
                    newbal=acoutbal-withdrawal_amount
print(f"new balance is{newbal}")

#23

username=input("enter usernme")
pass1=input("input your password")
if username == "admin" and pass1 == "12345":
    print("login secusesfull")
elif username != "admin":
    print("user not found")
elif pass1 != "12345":
    print("pass word is incorct")

#24

amount=int(input("enter your amount"))
if amount < 500:
        discount_percent = 0
elif amount <= 999:
        discount_percent = 5
elif amount <= 1999:
        discount_percent = 10
elif amount <= 4999:
        discount_percent = 15
else:  # ₹5000 and above
        discount_percent = 20

discount_amount = (amount * discount_percent) / 100
final_amount = amount - discount_amount

print(f"Original amount    : ₹{amount}")
print(f"Discount percentage: {discount_percent}%")
print(f"Discount amount    : ₹{discount_amount}")
print(f"Final amount       : ₹{final_amount}")

#25

Input marks for 3 subjects
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
# Check if any subject mark is invalid (not between 0 and 100)
if sub1 < 0 or sub1 > 100 or sub2 < 0 or sub2 > 100 or sub3 < 0 or sub3 > 100:
    print("Invalid marks! Marks must be between 0 and 100.")
# Check if student failed in any subject (below 35)
elif sub1 < 35 or sub2 < 35 or sub3 < 35:
    print("Result: FAIL (Failed in one or more subjects)")
else:
    # Calculate average
    avg = (sub1 + sub2 + sub3) / 3
    print(f"Average: {avg:.2f}")
    # Determine Grade based on average
    if avg >= 75:
        print("Grade: Distinction")
    elif avg >= 60:
        print("Grade: First Class")
    elif avg >= 50:
        print("Grade: Second Class")
    else:
        print("Grade: Pass")

#26

day = int(input("Enter Day: "))
month = int(input("Enter Month: "))
year = int(input("Enter Year: "))

if month < 1 or month > 12:
    print(f"{day:02d}/{month:02d}/{year} → Invalid (Month must be between 1 and 12)")
else:

    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    if month == 2:
        max_days = 29 if is_leap else 28
    elif month in [4, 6, 9, 11]:
        max_days = 30
    else:
       max_days = 31
    if 1 <= day <= max_days:
        print(f"{day:02d}/{month:02d}/{year} → Valid")
    else:
        print(f"{day:02d}/{month:02d}/{year} → Invalid")

#27

hours = int(input("Enter Hours (0-23): "))
minutes = int(input("Enter Minutes (0-59): "))
seconds = int(input("Enter Seconds (0-59): "))

if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
    print(f"\n{hours:02d}:{minutes:02d}:{seconds:02d} → Valid time")
else:
    print(f"\n{hours:02d}:{minutes:02d}:{seconds:02d} → Invalid time")


#28

name1 = input("Enter Name for Person 1: ")
age1 = int(input(f"Enter Age for {name1}: "))

name2 = input("Enter Name for Person 2: ")
age2 = int(input(f"Enter Age for {name2}: "))


name3 = input("Enter Name for Person 3: ")
age3 = int(input(f"Enter Age for {name3}: "))

print("\n--- Result ---")

if age1 == age2 == age3:
    print(f"All three ({name1}, {name2}, and {name3}) are of the same age.")

elif age1 == age2 and age1 < age3:
    print(f"{name1} and {name2} are the youngest.")

elif age1 == age3 and age1 < age2:
    print(f"{name1} and {name3} are the youngest.")

elif age2 == age3 and age2 < age1:
    print(f"{name2} and {name3} are the youngest.")

elif age1 < age2 and age1 < age3:
    print(f"{name1} is the youngest.")

elif age2 < age1 and age2 < age3:
    print(f"{name2} is the youngest.")

else:
    print(f"{name3} is the youngest.")

#29


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if (num2 < num1 < num3) or (num3 < num1 < num2):
    second_largest = num1

elif (num1 < num2 < num3) or (num3 < num2 < num1):
    second_largest = num2

else:
    second_largest = num3

print(f"\nThe second-largest number is: {second_largest}")

#30

age = int(input("Enter Age: "))
marks = float(input("Enter Marks: "))
income = float(input("Enter Family Income (₹): "))
attendance = float(input("Enter Attendance (%): "))


is_age_valid = 18 <= age <= 25
is_marks_valid = marks >= 85
is_attendance_valid = attendance >= 75
is_income_valid = income <= 300000


if is_age_valid and is_marks_valid and is_attendance_valid and is_income_valid:
    print("\nScholarship Approved")
else:
    print("\nScholarship Rejected")
    print("Reason:")
    
    if not is_age_valid:
        print("- Age must be between 18 and 25")
    if not is_marks_valid:
        print("- Marks below 85")
    if not is_attendance_valid:
        print("- Attendance below 75%")
    if not is_income_valid:
        print("- Family income above ₹300,000")

for addition of number in 3 digit number

a=int(input("enter your number"))
b=a%10
c=a//10
d=c%10
e=c//10
print(b+d+e)