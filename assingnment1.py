#python
#Q.1 Check if a number is positive, negative, or zero.

n = int(input("Enter number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

#Q.2 Check whether a number is even or odd.
n = int(input("Enter number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

#Q.3 Find the greater of two numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is greater")
else:
    print("Second number is greater")

 #Q.4 Find the greatest of three numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("A is greatest")
elif b > c:
    print("B is greatest")
else:
    print("C is greatest")

#Q.5 Check if a person is eligible to vote (age ≥ 18).
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

#Q.6Check whether a year is a leap year.
year = int(input("Enter year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#Q7 Check if a character is a vowel or consonant.
ch = input("Enter a character: ")

if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")

#Q.8 Check whether a number is divisible by 5 and 11.
n = int(input("Enter a number: "))

if n % 5 == 0 and n % 11 == 0:
    print("Divisible by 5 and 11")
else:
    print("Not divisible")

#Q.9 Check if a number is a multiple of both 3 and 7.
    n = int(input("Enter a number: "))

if n % 3 == 0 and n % 7 == 0:
    print("Multiple of both 3 and 7")
else:
    print("Not a multiple")

#Q.10 Assign grades based on marks:
#a.90–100: A
#b.80–89: B
#c.70–79: C
#d.60–69: D
#e.Below 60: F
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")

#Q.11 Check if a character is uppercase or lowercase.
ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase")
else:
    print("Lowercase")

#Q.12 Find whether the entered alphabet is a vowel using if-elif.
ch = input("Enter an alphabet: ")

if ch == 'a':
    print("Vowel")
elif ch == 'e':
    print("Vowel")
elif ch == 'i':
    print("Vowel")
elif ch == 'o':
    print("Vowel")
elif ch == 'u':
    print("Vowel")
else:
    print("Consonant")   

#Q.13 Check if three sides can form a triangle.
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    print("Triangle is possible")
else:
    print("Triangle is not possible")

#Q.14  Determine the type of triangle (Equilateral, Isosceles, Scalene).
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b and b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

#Q.15  Find the largest among four numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a > b and a > c and a > d:
    print("A is largest")
elif b > c and b > d:
    print("B is largest")
elif c > d:
    print("C is largest")
else:
    print("D is largest")

#Q.16 Check whether a number is a three-digit number.
n = int(input("Enter a number: "))

if n >= 100 and n <= 999:
    print("Three-digit number")
else:
    print("Not a three-digit number")

#Q.17 Calculate electricity bill using slab rates.
#Q.18  Calculate income tax based on income slabs.
#Q.19 Check if a student passes (minimum 35 marks in each subject).
a = int(input("Enter marks of subject 1: "))
b = int(input("Enter marks of subject 2: "))
c = int(input("Enter marks of subject 3: "))

if a >= 35 and b >= 35 and c >= 35:
    print("Pass")
else:
    print("Fail")

#Q.20  Find whether a number is within a given range.
n = int(input("Enter a number: "))

if n >= 10 and n <= 50:
    print("Number is within range")
else:
    print("Number is outside range")

#Q.21 Build a simple calculator using if-elif-else (+, -, *, /).
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result =", a + b)
elif op == "-":
    print("Result =", a - b)
elif op == "*":
    print("Result =", a * b)
elif op == "/":
    print("Result =", a / b)
else:
    print("Invalid operator")

#Q.22 Check if a year is a century leap year.
year = int(input("Enter year: "))

if year % 100 == 0 and year % 400 == 0:
    print("Century Leap Year")
else:
    print("Not a Century Leap Year")

#Q.23 Determine the season based on the month number.
#Q.24 Find the number of days in a month.
#Q.25 Check whether a password meets minimum conditions (length, digits, etc.).
#Q.26Determine ticket price based on age category.
#Q.27Calculate discount based on purchase amount.
#Q.28Check if a person is eligible for a driving license (age and eyesight condition).
#Q.29Create a login system with username and password validation.
#Q.30Create a menu-driven program using if-elif-else with options like:
#Addition
#Subtraction
#Multiplication
#Division
#Exit
          