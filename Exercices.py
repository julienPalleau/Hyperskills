########################################################################################################################
"""
Calculate a remainder
Write a program that calculates the remainder of 10 divided by 3 and prints the result.
"""
# print(10 / 3)
# print(10 % 3)

########################################################################################################################
"""
Knowledge verification: Multi-line programs

Write the code that will print all days of the week on separate lines with an empty line between them. Make sure that 
each day starts with a capital letter. Start it with Sunday.
"""
# print("Sunday")
# print()
# print("Monday")
# print()
# print("Tuesday")
# print("")
# print("Wednesday")
# print("")
# print("Thursday")
# print("")
# print("Friday")
# print("")
# print("Saturday")

########################################################################################################################
"""
Program with numbers 
The first digit of a two-digit number

Write a program that takes a two-digit integer as an input and prints its first digit (i.e., the number of tens).
"""
# number = input()
# print(int(number[0]))

########################################################################################################################
"""
Program with numbers 
Calculating an expression

Write a program that reads an integer value n from the standard input and prints the result of the expression:
((n + 1) * n + 2) * n + 3
"""
# n = int(input())
# print(((n + 1) * n + 2) * n + 3)

########################################################################################################################
"""
Program with numbers
Calculating S V P

Ask the user about parameters of a rectangular parallelepiped (3 integers representing the length, width, and height) 
and print the sum of edge lengths, its total surface area, and the volume, one answer per line.

Sum of lengths of all edges:
s=4(a+b+c)s = 4(a + b + c)s=4(a+b+c)

Surface area:
S=2(ab+bc+ac)S = 2(ab + bc + ac)S=2(ab+bc+ac)

Volume:
V=abcV = abcV=abc
"""
# a = int(input())
# b = int(input())
# c = int(input())
# s = 4 * (a + b + c)
# S = 2 * (a * b + b * c + a * c)
# V = a * b * c
# print(s)
# print(S)
# print(V)

########################################################################################################################
"""
Program with numbers 
Desks

Wow! This problem is kind of tricky. If you're ready to put your thinking cap on, brace yourself and good luck! 
Otherwise, you can skip it for now and return any time later.

A school has decided to create three new math groups and equip three classrooms for them with new desks. Your task is to 
calculate the minimum number of desks to be purchased. To do so, you'll need the following information:

    The number of students in each of the three groups is known: your program will receive three non-negative integers 
    as the input. It is possible that one or more of them will be zero, so you should take it into account.
    Each group will sit in its own classroom. It means that you should calculate the number of desks for each classroom 
    separately, and only then add them up!
    At most two students may sit at any desk. You are expected to output the minimum number of desks to buy, so there 
    should be as many as possible desks taken by two students rather than one.

Most probably, you'll need operations // and % in your program!
"""
# number_1 = int(input())
# number_2 = int(input())
# number_3 = int(input())
# total = [number_1, number_2, number_3]
# nb_desk = 0
# for number in total:
#     nb_desk += number // 2 + number % 2
# print(nb_desk)

########################################################################################################################
"""
Program with numbers
Savings account

For the given amount of money, calculate the income from this savings account with a 5% interest rate after one year.

Here's the formula for calculating the income: income=amount×interest×years/100

Save the result into the variable income. You DO NOT need to print it.
"""
# amount = 1000
# interest_rate = 5
# years = 1
# # change the next line
# income = 1000 * 5 * 1 / 100
# print(income)

########################################################################################################################
"""
Program with numbers
Difference of times

You will get the values for two moments in time of the same day: when Megan went for a walk, and when it started to 
rain. It is known that the first event happened earlier than the second one. Find out how many seconds passed between 
them.

The program gets the input of six integers, each on a separate line. The first three integers represent hours, minutes, 
and seconds of the first event, and the rest three integers define similarly the second event. Print the number of 
econds between these two moments of time.
"""
# hours_first = int(input())
# minutes_first = int(input())
# seconds_first = int(input())
# hours_second = int(input())
# minutes_second = int(input())
# seconds_second = int(input())
#
# print((hours_second - hours_first) * 3600 + (minutes_second - minutes_first) * 60 + (seconds_second - seconds_first))

########################################################################################################################
"""
Program with numbers
The sum of digits

Given a three-digit integer (i.e., an integer from 100 to 999), find the sum of its digits and print the result.

To get the separate digits of the input integer, make use of % and // (for example, you can get 8 from the number 508 
by taking the remainder of the division by 10).
"""
# number = int(input())
# result = []
#
# while number > 0:
#     unit = number % 10
#     number //= 10
#     result.append(unit)
#
# print(sum(result))

########################################################################################################################
"""
Program with numbers
Divide nuts equally between squirrels

N squirrels found K nuts and decided to divide them equally. Determine how many nuts each squirrel will get and print 
the result.
Input data format
There are two positive numbers N and K, each of them is not greater than 10000.
"""


########################################################################################################################
# n = int(input())
# line_list = list(range(1, 2 * n, 2))  # create list of n odd numbers [1, 3, 5, etc.]
# line_max = max(line_list)  # get max width in order to be centered
# for line in line_list:
#     print(('#' * line).center(line_max))

########################################################################################################################
"""
What day is it?
Read a date from the input given in one of the following formats: YYYY-MM-DD or YYY-MM-DD. Print the year, month and day
on separate lines.
"""
# date = input()
# year, month, day = date.split("-")
# print(year)
# print(month)
# print(day)
########################################################################################################################
"""
Find positions
Write a program that reads a sequence of numbers from the first line and the number x from the second line. Then it 
should output all positions of x in the numerical sequence.
The position count starts from 0. In case x is not in the sequence, print the line "not found" (quotes omitted, 
lowercased).
Positions should be displayed in one line, in ascending order of the value.
"""

# input_string = input()
# my_list = input_string.split()
# str_to_int = list(map(int, my_list))
# number = int(input())
# result = []
# test = False
#
# for ind, num in enumerate(str_to_int):
#     if num == number:
#         result.append(ind)
#         test = True
# res = []
# if test:
#     [res.append(ind) for ind, num in enumerate(str_to_int) if num == number]
#     [print(line, end=" ") for line in res]
# else:
#     print("not found")

########################################################################################################################
"""
- Split and join -
String tricks
Examine the code and fix the mistakes so that the join() method works.
random_numbers = [1, 22, 333, 4444, 55555]
print("\n".join(random_numbers))
"""
# random_numbers = [1, 22, 333, 4444, 55555]
# print("\n".join([str(i) for i in random_numbers]))

########################################################################################################################
"""
- Split and join -
Prepositional genitive
Advanced input() handling is used to read input directly into several variables, for example:
x, y = input().split()
"""
# x, y = input().split()
# print(f"{x} of {y}")

########################################################################################################################
"""
- Split and join -
Straight A's
Write a program that calculates the proportion of students who received grade A.
A five-point rating system with grades A, B, C, D, F is used.
Input format:
A string with students' marks separated by space. At least one mark will be present.
Output format:
A fractional number with exactly two decimal places.
To format the decimal places use the round(number, places) function.
"""
# notes = input()
# notes = notes.split()
# print(len(notes))
# print(round(notes.count("A")/len(notes), 2))

########################################################################################################################
"""
- Split and join -
Flip
Let's try to reverse a numeric sequence. Read it from the input and print its numbers in reverse order separated by 
spaces.
"""
# # solution 1
# sequence = input().split()
# [print(num, end=" ") for num in sequence[::-1]]
# print()
#
# # solution 2
# sequence = input().split()
# print(" ".join(sequence[::-1]))

########################################################################################################################
"""
- Split and join -
Find words
Find all words that end in "s" and print them together separated by an underscore.
After such words there will be no punctuation marks, you do not need to worry about that.
"""
# # Solution 1
# sentence = input().split()
# result = ""
# for word in sentence:
#     if word[-1] == "s":
#         result += word + "_"
#
# print(result[:len(result)-1:])
#
# # Solution 2
# sentence = input().split()
# new = []
# for word in sentence:
#     if word.endswith('s'):
#         new.append(word)
# print("_".join(new))

########################################################################################################################
"""
- Split and join -
mixedCase

Convert a text into lowerCamelCase, or mixedCase.
The input format:
A lowercased word or several words separated by spaces.
The output format:
Print this text stylized as mixedCase, that is, the first word should be in lowercase and all other words – capitalized.
"""
# # Solution 1
# text = input().split()
# result = text[0]
# i = 0
# for word in text:
#     if i != 0:
#         result += word.capitalize()
#     i += 1
# print(result)
#
# # Solution 2
# word = input().title().split()
# word[0] = word[0].lower()
# print("".join(word))

########################################################################################################################
"""
- Split and join -
Spellchecker 

Write a spellchecker that tells you which words in the sentence are spelled incorrectly. Use the dictionary in the code 
below.
The input format:
A sentence. All words are in the lowercase.
The output format:
All incorrectly spelled words in the order of their appearance in the sentence. If all words are spelled correctly, 
print OK.
dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
"""
# dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
#               'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
#               'sign', 'the', 'to', 'uncertain']
#
# test = True
# sentence = input().split()
# for word in sentence:
#     if word in dictionary:
#         pass
#     else:
#         print(word)
#         test = False
#
# if test:
#     print("OK")

########################################################################################################################
"""
- Split and join -
Fix the mistakes

The code below is supposed to find all website addresses (https://, http://, www.) in the input text. However, it is 
not finished. Complete the code and print all the addresses in the order in which they appear in the text, each on a 
new line. Mind that str.lower() can help you to convert all characters of the string to the lower case.
"""
# # Solution 1
# import re
# text = input()
# words = text.split()
# for word in words:
#     r1 = re.search(r"([w+W+]{3}.*)", word)
#     if r1:
#         print(r1.group(0))

# # Solution 2
# text = input()
# words = text.split()
# for word in words:
#     if word.lower().startswith("www.") or word.lower().startswith("https://") or word.lower().startswith("http://"):
#         print(word)

# # Solution 3
# text = input().split()
# addresses = ("https://", "http://", "www.")
#
# for word in text:
#     if word.lower().startswith(addresses):
#         print(word)

########################################################################################################################
"""
- Split and join -
CapWords

In Python, the names of classes (you'll learn about them in detail later) follow the CapWords convention. Let's convert 
the input phrase accordingly by capitalizing all words and spelling them without underscores in-between.
The input format:
A word or phrase, with words separated by underscores, like function and variable names in Python.
You might want to change the case of letters since they are not necessarily lowercased.
The output format:
The name written in the CapWords fashion.
"""
# sentence = input()
# result = sentence.split("_")
# res = ""
# for word in result:
#     res += word.capitalize()
# print(res)

########################################################################################################################
"""
Work on project. Stage 1/4 Mini-calculator
Mini-calculator

Description

People learn new things in one way or another. Learning sometimes means that you need to check your comprehension by 
taking a test. It also requires a person (or a program) to check your answers. You may have been in a situation when 
you think that you have solved the task correctly, but your professor has a different (sometimes wrong!) answer. It 
happens; everybody makes mistakes.
Not our application though. It should calculate the solution in a very precise manner. We need to make a simple 
calculator that can evaluate expressions like a + b, a - b, or a * b. We will leave the division aside for now.
Objectives

    A user inputs a line that looks like a simple mathematical operation.
    The application should print the result of the operation.

Examples

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.
"""

# entry = input().split()
#
# if entry[1] == '+':
#     print(int(entry[0]) + int(entry[2]))
# elif entry[1] == '-':
#     print(int(entry[0]) - int(entry[2]))
# elif entry[1] == '*':
#     print(int(entry[0]) * int(entry[2]))

########################################################################################################################
"""
Declaring a function 
Fahrenheit 

Convert the temperature from Fahrenheit to Celsius in the function below. You can use this formula:

C∘=(F∘−32)×59C^\circ = (F^\circ - 32)\times \frac{5}{9}C∘=(F∘−32)×95​

Round the returned result to 3 decimal places.

You don't have to handle input, just implement the function below.

Also, make sure your function returns the value. Please do NOT print anything.
"""

# def fahrenheit_to_celsius(fahrenheit):
#     return round((fahrenheit - 32) * 5 / 9, 3)
#
#
# print(fahrenheit_to_celsius(451))

########################################################################################################################
"""
Declaring a function 
Make the function work

The function closest_higher_mod_5 takes exactly one integer argument x and returns the smallest integer y such that:

    y is greater than or equal to x,
    y is divisible by 5.

Correct the last line of the code below to make the function work.

def closest_higher_mod_5(x):
    remainder = x % 5
    if remainder == 0:
        return x
    return "I don't know :("
"""

# def closest_higher_mod_5(x):
#     remainder = x % 5
#     while remainder > 0:
#         x += 1
#         remainder = x % 5
#     else:
#         return x if remainder == 0 else "I don't know :("
#
#
# print(closest_higher_mod_5(43))

########################################################################################################################
"""
Declaring a function 
Captain

Define a function that will add the word "captain" before the name of a person. The function should be named 
captain_adder, take one argument name, and print the string, i.e. it doesn't have to return anything. You don't need to 
call your function, only implement it. Also, you don't need to take input, use only the name variable that should be an 
argument of the function. 
"""

# def captain_adder(name):
#     print("captain ", name)
#
# captain_adder("Julien")

########################################################################################################################
"""
Declaring a function 
Prevent cheating

On Hyperskill, we sometimes need to check that the student's code doesn't use a particular method. For instance, when 
the task is to manually implement the factorial computation instead of using the factorial() function from the math 
module. How could we do that?

It is straightforward. We can override math.factorial() to do something else — raise an error or print a message to the 
student. To do so, first, we define a function that does what we want (for example, prints a message) with the same 
arguments (since we want to disguise our new function as the original one). Then, outside this new function body, we 
need to assign it to math.factorial this way: math.factorial = new_math_factorial (pay attention to the absence of 
parentheses). Now, if the student tries to use math.factorial, our custom function will be raised. It happens because 
when multiple functions with the same name exist, the later one always overrides the prior.

In this task, you are a content creator at Hyperskill. Implement the example with the factorial yourself. Your program 
should override math.factorial() and make it print the message Don't cheat! instead of calculating a factorial. 
"""
# import math
#
# # your code here
#
#
# def new_math_factorial(number):
#     print("Don't cheat!")
#
#
# math.factorial = new_math_factorial
#
# # don't delete this line, please
# math.factorial(23)

########################################################################################################################
"""
Else statement
Spellchecker

Whoa! This problem requires knowledge of list collection type. If you're feeling up to the challenge, brace yourself, 
and good luck! Otherwise, you can skip it for now and return any time later.
Write a simple spellchecker that tells you if the word is spelled correctly. Use the dictionary in the code below: it 
contains the list of all correctly written words.

The input format:
A single line with the "word".

The output format:
If the word is spelled correctly write Correct, otherwise, Incorrect. 
dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]
"""
# dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]
#
# word = input()
# Solution1:
# if word in dictionary:
#     print("Correct")
# else:
#     print("Incorrect")

# Solution2:
# print("Correct" if word in dictionary else "Incorrect")

########################################################################################################################
"""
Else statement
The Maximum
Here is a program which finds the maximum of two numbers. Guess what it will print for the variables a = 9, b = 9 and 
select the line of the code that will give such a result.

if a > b:
    print(a)
else:
    print(b)
"""

# if a > b:
#     print(a)
# else:
#     print(b)

########################################################################################################################
"""
Else statement
Minimum and maximum 

Imagine that your friend asked you to write a program that finds the minimum and the maximum.
Write a program that receives two integers as its input, each number goes on a new line. The output should show:
    The biggest number in the first line
    The smallest number in the second line.
Note that your friend might insert identical numbers! In this case, just output both given numbers on separate lines.
"""
# first_number = int(input())
# second_number = int(input())
#
# if first_number > second_number:
#     print(first_number)
#     print(second_number)
# elif second_number > first_number:
#     print(second_number)
#     print(first_number)
# else:
#     print(first_number)
#     print(second_number)

########################################################################################################################
"""
Else statement
Triangle or not triangle

Read three angles given on separate input lines and check whether they form a triangle. Print the answer in the 
following format: "The triangle is valid!" or "The triangle is not valid!".
"""
# sum_triangle_angles = 180
# angles = []
# for _ in range(0, 3):
#     angles.append(int(input()))
#
# if sum(angles) == sum_triangle_angles:
#     print("The triangle is valid!")
# else:
#     print("The triangle is not valid!")

########################################################################################################################
"""
Else statement
Opposite Sign

Read an integer as input and print it with the opposite sign.
"""
# number = int(input())
# print(-number)

########################################################################################################################
"""
While loop
Rich man's world

When a bank has financial problems the government can return a client's deposit if it is less than 700,000. The 
interest rate for a particular deposit is 7.1% a year. The percentages are paid to the same deposit at the end of the 
year and a new value of the interest is calculated.
Find out how many years it will take for the sum of the deposit to exceed the value protected by the government.

The input format:
The initial sum of the deposit. It is guaranteed that the value will be between 50,000 and 700,000.

The output format:
The number of years.
"""
# initial_deposit = int(input())
# ir = 7.1
# allowed_returned_deposit = 700000
# new_account_value = 0
# year = 0
# new_account_value += initial_deposit
#
# while new_account_value < allowed_returned_deposit:
#     new_account_value += new_account_value * ir / 100
#     year += 1
#
# print(year)

########################################################################################################################
"""
While loop
Favor

Carl asks you to count the sum of the first k natural numbers. Read k from the input, then add up numbers from 1 to k 
and print your answer.
"""

# k = int(input())
# print(sum(range(0, k + 1)))

########################################################################################################################
"""
While loop
Half-life

In nuclear physics, the half-life is used to describe the rate with which elements undergo radioactive decay. More 
precisely, it is the time required for an element to reduce in half.

Let's take an isotope of Radium (Ra) called radium-223. Its half-life is about 12 days: this means that every 12 days 
the number of atoms reduces in half.

Your program should:

    read the initial and the final quantity of atoms from the input.
    count how many complete half-life periods it would take for the initial number of atoms of radium-223 to become 
    equal to or go below the final quantity. Note that the number of half-life periods should be an integer, not a float!
    multiply the number of half-life periods by 12 to convert the number of half-life periods to days.
    output the resulting number of days that it takes for the initial number of atoms to go below the final number.

For example, the initial number of atoms is 4 and the resulting quantity is 3. After the first half-life period, the 
initial number will reduce to 2 atoms, which is below 3. Then, we take the number of half-life periods that have passed 
(1) and multiply it by the number of days that every half-life period takes (12). The output will be 12.
The input format:

The first line: the initial quantity of atoms (from 2 to 1,000,000).
The second line: the final quantity of atoms.

The output format:

The number of days that it would take for radium-223 to go from the initial quantity of atoms to or below the final 
quantity of atoms.
An example:
The initial quantity is 8, the final quantity is 3. Your program output should be number 24.
"""
########################################################################################################################

# initial_quantity = int(input())
# final_quantity = int(input())
# half_period = 12
# number_of_half_period = 0
#
# while initial_quantity >= final_quantity:
#     number_of_half_period += 1
#     initial_quantity -= int(initial_quantity / 2)
#
# print(number_of_half_period * 12)