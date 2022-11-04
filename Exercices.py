########################################################################################################################
"""
Calculate a remainder
Write a program that calculates the remainder of 10 divided by 3 and prints the result.
"""
# print(10 / 3)
# print(10 % 3)

########################################################################################################################
from typing import List

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
# N = int(input())
# k = int(input())
# print(k // N)

########################################################################################################################
"""
Program with numbers
How many nuts will be left after division

Some squirrels found some nuts and decided to divide them equally. You will get the number of squirrels and the number 
of nuts as input on separate lines. Find out how many nuts will be left after each of the squirrels takes an equal 
number of nuts. Print the result.
"""
# N = int(input())
# k = int(input())
# print(k % N)

########################################################################################################################
"""
Program with numbers
The last digit of a number
Write a program that reads an integer and outputs its last digit.
"""
# number = list(input())
# print(number[-1])

########################################################################################################################
"""
Program with numbers
Good rest on vacation
Write a program that will help people who are going on vacation. The program should calculate the total required sum 
(e.g. $) of money to have a good rest for a given duration.

There are four parameters that have to be considered:

    duration in days
    total food cost per day
    one-way flight cost
    cost of one night in a hotel (the number of nights is equal to the duration of days minus one)

Read integer values of these parameters from the standard input and then print the result.
"""
# duration_days = int(input())
# food_cost_per_day = int(input())
# flight_cost = int(input())  # one way
# hotel_cost = int(input())  # one night
#
# print(f"{duration_days * food_cost_per_day + (duration_days - 1) * hotel_cost + 2 * flight_cost}")
########################################################################################################################
# n = int(input())
# line_list = list(range(1, 2 * n, 2))  # create list of n odd numbers [1, 3, 5, etc.]
# line_max = max(line_list)  # get max width in order to be centered
# for line in line_list:
#     print(('#' * line).center(line_max))

########################################################################################################################
"""
Invoking a function
Young and beautiful

Read the input three times. Each one contains the age of a person – Jack's, Alex's, and Lana's. Find the youngest one 
among them and print this person's age.
"""
# jack_age = int(input())
# alex_age = int(input())
# lana_age = int(input())
#
# print(min(jack_age, alex_age, lana_age))

########################################################################################################################
"""
Invoking a function
Hello, world!

The classical introductory exercise, slightly modified. Write a program that takes a string, writes it to the variable 
name (this part of code is already written for you), and then prints "Hello, world! Hello, name". Note that there's a 
space before the name.
The variable name is already defined.
"""
# name = input()
# print(f"Hello, world! Hello, {name}")

########################################################################################################################
"""
Invoking a function
Longest word

Find the longest word in a pair and print its length.
The variables word1 and word2 are defined for you.
"""
# mot1 = input()
# mot2 = input()
# print(max(len(mot1), len(mot2)))

########################################################################################################################
"""
Create module
Create module

Below there is a custom Python module:

# my_module.py

name = "John"

def printer(x):
    print("Hello,", x)

You have already imported this module into your code:

import my_module

Write a line of the code that will now call the function printer() on the name variable. Mind that both the variable 
and the function are defined in my_module.py!
"""
# import my_module
#
# my_module.printer(my_module.name)

########################################################################################################################
"""
Create module
Function main()
Let's say you need a module that:

    stores a string variable n with the value "42".
    defines a main() function that prints the value of n.
    calls the main() function only if it is executed as a script.

Put the lines of this module's code in the correct order and add indents. The first line of the program must be 
n = "42". NB: Use the buttons on the left to add indentation (one click equals four spaces).
"""
# n = "42"
#
#
# def main():
#     print("N:", n)
#
#
# if __name__ == "__main__":
#     main()

########################################################################################################################
"""
Errors
Chaos
Look at the code below and eliminate the chaos: the first line should print the resulting number of the calculation and 
the second line should print the word mathematics.
print("45/9 + 16*(5 + 8)")
print(mathematics)
"""
# print(45/9 + 16*(5 + 8))
# print("mathematics")

########################################################################################################################
"""
Errors
Locate a problem
The code snippet below needs debugging. Examine it and write down the line number on which the compilation of code will stop.

print( "The quick brown fox" )  # 1
print()                         # 2
print'jumps')                   # 3
pint()                          # 4
print( ' over the lazy dog  )   # 5

answer: 3
"""

########################################################################################################################
"""
Errors
Locate a problem
I am = I'm
I have = I've
I will = I'll
I had / would = I'd
"""
# print("I am = I'm")
# print("I have = I've")
# print("I will = I'll")
# print("I had / would = I'd")

########################################################################################################################
"""
Errors
Locate a problem
Take a look at the following code. Did we declare all variables correctly, according to Python's syntax? Try to fix all 
mistakes, so that SyntaxError will not be raised during the initialization of these variables.
hope = "I hope this is actually going to work'
doubt = 'Do I need to double check all lines?'
suggestion = "What if I write it in "double quotes"?
"""
# hope = "I hope this is actually going to work"
# doubt = 'Do I need to double check all lines?'
# suggestion = 'What if I write it in "double quotes"?'

########################################################################################################################
"""
List comprehension
Else comprehension
# the following line reads the list from the input, do not modify it, please
old_list = [int(num) for num in input().split()]

binary_list = # your code here
print(binary_list)
"""
# old_list = [int(num) for num in input().split()]
# print(old_list)
#
# binary_list = [1 if i > 0 else 0 for i in old_list]
# print(binary_list)

########################################################################################################################
"""
List comprehension
Plus one
You are given a list of strings containing integer numbers. Print the list of their values increased by 1.
E.g. if list_of_strings = ["36", "45", "99"], your program should print the list [37, 46, 100].
The variable list_of_strings is already defined, you don't need to work with the input or define it again.
"""
# list_of_strings = [int(num) for num in input().split()]
# print([int(i) + 1 for i in list_of_strings])

########################################################################################################################
"""
List comprehension
Length
Given a list of words in the code below, create a list of lengths of those words and print it.
words = ["apple", "it", "creek", "pelican", "subsequent", "horse", "apothecary"]
"""
# words = ["apple", "it", "creek", "pelican", "subsequent", "horse",
#          "apothecary"]
# list_of_length = [len(word) for word in words]
# print(list_of_length)

########################################################################################################################
"""
List comprehension
Boundary
Write a program that divides numbers into two lists depending on whether they are greater than or less than 5. You don't
 have to include number 5 itself.
A sequence of numbers has been read from the input for you.
# work with a list from this variable
numbers = [int(n) for n in input()]

# change the next two lines
less_than_5 = ...
greater_than_5 = ...

# printing your results
print(less_than_5)
print(greater_than_5)
"""
# # work with a list from this variable
# numbers = [int(n) for n in input().split()]
#
# # change the next two lines
# less_than_5 = [number for number in numbers if number < 5]
# greater_than_5 = [number for number in numbers if number > 5]
#
# # printing your results
# print(less_than_5)
# print(greater_than_5)

########################################################################################################################
"""
List comprehension
Even numbers

Write a program that takes a list of numbers, creates another list of even numbers from the first list, and prints it.

E.g. if my_numbers = [1, 2, 3, 4, 5], then your program should print the list [2, 4].

# the following line reads the list from the input; do not modify it, please
my_numbers = [int(x) for x in input().split(" ")]

# work with the variable 'my_numbers'
"""
# # the following line reads the list from the input; do not modify it, please
# my_numbers = [int(x) for x in input().split(" ")]
#
# # work with the variable 'my_numbers'
# result = [number for number in my_numbers if number % 2 == 0]
# print(result)

########################################################################################################################
"""
List comprehension
The mean

Given a numeric sequence at the input, create a list in which each number will be a digit from this input string. Then 
use this list to calculate the arithmetic mean, that is, the sum of all the digits divided by their total count.
Don't forget to print your result.
"""
# test = [float(i) for i in list(input())]
# print(sum(test) / len(test))


########################################################################################################################
"""
List comprehension
How many days?

The list seconds is a list of numbers that represent seconds. Convert the number of seconds to full days and print the 
list that contains these values. The number of full days should be an int value.
seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# create a list of days here
"""
# seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# nb_days = [second // (3600 * 24) for second in seconds]
# print(nb_days)

########################################################################################################################
"""
List comprehension
Threefold

Print a list of numbers from 1 to 1000 that can be divided by 3.
"""
# list_of_numbers = [print(x) for x in range(0, 1001) if x % 3 == 0]
#
# # or to get it validated
# list_of_numbers = [x for x in range(1, 1001) if x % 3 == 0]
# print(list_of_numbers)

########################################################################################################################
"""
List comprehension
Vowels

Read a string from the input and print a list of vowels that belong to that string.
All vowels are enlisted in a variable of the same name.

vowels = 'aeiou'
# create your list here
"""
# vowels = 'aeiou'
# string = input()
# vowels_list = [letter for letter in string if letter in vowels]
# print(vowels_list)

########################################################################################################################
"""
List comprehension
Odd numbers

Read a string with digits from the input and convert each number to an integer. Create a list in which you should 
include only odd digits. Finally, print what you'll get.

Sample Input 1:
87113420

Sample Output 1:
[7, 1, 1, 3]
"""
# list_numbers = input()
# print([int(i) for i in list_numbers if int(i) % 2 == 1])

########################################################################################################################
"""
List comprehension
A list of words

Write a program that takes a list with words, creates a new list of words that start with the letter "a" in the first 
list, and prints it.
Some words may begin with the capital A! Leave them in their original form in the resulting list.
E.g. if words = ['apple', 'pear', 'banana', 'Ananas'], then your program should print the list ['apple', 'Ananas'].
The list with words is already defined: you can access it using the variable words.
"""
# words = ['apple', 'pear', 'banana', 'Ananas']
# words = [word for word in words if word.startswith("a") or word.startswith("A")]
# print(words)

########################################################################################################################
"""
List comprehension
Running total

Given a numeric sequence, create a list in which each number will be a digit from this input string. Then use this list 
to calculate the running total, or cumulative sum. Essentially, it's a new list of partial sums that gets updated every 
time a new element appears.
For example, we can transform the list [1, 2, 3] to [1, 1 + 2, 1 + 2 + 3], which equals to [1, 3, 6].
"""
# Solution 1
# prior python 3.8


# list_numbers = list(input())
# list_beta = [int(number) for number in list_numbers]
# j = 0
# result=[]
# for i in list_beta:
#     i += j
#     j = i
#     result.append(i)
#
# print(result)


# Solution 2
# works only for python 3.8 and above
# list_numbers = list(input())
# result = 0
# print([result := result + int(list_numbers[i]) for i in range(len(list_numbers))])

# Solution 3
# numbers = [int(x) for x in list(input())]
# new_list = [sum(numbers[:i + 1]) for i, x in enumerate(numbers)]
# print(new_list)

# Rappel
# test = [0, 1, 2, 3, 4, 5]
# print(test[:6])

########################################################################################################################
"""
Any and all
Prime numbers

In math, we call a natural number prime if it's greater than 1 and can be divided without any remainder only by 1 and 
itself:
2, 3, 5, 7, 11, 13, 17, ...
Create a list of all prime numbers up to 1000 in the code below. Just save this list into a variable prime_numbers, 
you don't have to print anything.
Make use of any() or all() to check if a number n leaves a zero remainder when divided by values from 2 to n - 1 
(inclusively).
"""
# prime_numbers = [n for n in range(2, 1001) if all(n % x for x in range(2, n))]
# print(prime_numbers)

########################################################################################################################
"""
Any and all
Competition

Today you are taking part in the chess competition. The winner of the competition will get the 'winner' status and the 
largest amount of money if they win all the games. Much is at stake!
The results are stored in a list. Fill the blanks in the code below and figure out how much money you won.
You DON'T need to print the answer.
check = ...([True, True, 1, 1, True])

if ...:
    status = 'winner'
else:
    status = 'loser'

if status == ...:
    winning_sum = 100
else:
    winning_sum = 10
"""
# check = all([True, True, 1, 1, True])
#
# if check:
#     status = 'winner'
# else:
#     status = 'loser'
# print(status)
#
# if status == 'winner':
#     winning_sum = 100
# else:
#     winning_sum = 10
# print(winning_sum)

########################################################################################################################
"""
Any and all
Heads or Tails

We have tossed a coin 6 times and saved the results in a list called heads_or_tails. The values are integers: 1 stands 
for a head, while 0 denotes a tail.
Add some code to find out whether the list has any heads. Do not print the variable check, just store the result in it.
# Fingers crossed
check =  # are there any heads in the list heads_or_tails?
"""
# heads_or_tails = [0, 0, 0 ,0, 0, 0, 0, 0]
# check = any(heads_or_tails)
# print(check)

########################################################################################################################
"""
Any and all
Lottery

Imagine that you have bought a bunch of lottery tickets and wrote down their numbers into the list. Now, it's time to 
figure out whether you have a winning ticket.
You know that all winning tickets are no less than 44. Fill the empty fields in the code (these ones ...) to check if 
you have at least one winning ticket.
You DON'T need to print the answer.
# As luck would have it
tickets = [11, 22, 33, 44, 55]
winning_tickets = [i >= ... for i in ...]
tickets_bool = ...(winning_tickets)
"""
# # As luck would have it
# tickets = [11, 22, 33, 44, 55]
# winning_tickets = [i >= 44 for i in tickets]
# tickets_bool = any(winning_tickets)
# print(tickets_bool)
# print(any("the object"))

########################################################################################################################
"""
Exception handling
Implementing logic

Advanced input() handling is used to read input directly into several variables, e. g.,
name, surname = input().split(), but a user still can enter more or fewer words.
In this task, you have to make sure that the user entered the necessary amount of words and...
    If there are more or fewer words in the input, print an error: "You need to enter exactly 2 words. Try again!"
    If everything's good, greet the user personally.
"""
# try:
#     name, surname = input().split()
# except Exception:
#     print("You need to enter exactly 2 words. Try again!")
# else:
#     print(f"Welcome to our party, {name} {surname}")

########################################################################################################################
"""
Exception handling
Zero

You know how to catch the built-in exceptions. Right now, try to read two numbers (a, b) and find the result of their 
division. Your main task it to catch the ZeroDivisionError. If there's an error, print the following message: 
The Error!. Otherwise, print the result of the division.
a = int(input())
b = int(input())
"""
# a = int(input())
# b = int(input())
#
# try:
#     print(a / b)
# except ZeroDivisionError:
#     print("The Error!")

########################################################################################################################
"""
Exception handling
Chatty bot
The original exercise consist in re-ordering the code below:
finally:
print("Hope to see you soon!")
print("What a beautiful name you have!")
except NameError:
try:
print("Hello, stranger!")
print("Hello,, name")

"""
# try:
#     print("Hello,, name")
# except NameError:
#     print("Hello, stranger!")
# else:
#     print("What a beautiful name you have!")
# finally:
#     print("Hope to see you soon!")

########################################################################################################################
"""
Exception handling
Modeling situation

Your program will have access to the exception_test() function, which can throw exceptions.
You need to write code that runs this function, then catches ArithmeticError, AssertionError, ZeroDivisionError 
exceptions and prints the name of the caught exception. Mind the hierarchy of exceptions.
An example solution that you should send for review:
try:
    exception_test()
except Exception:
    print("Exception")
except BaseException:
    print("BaseException")
"""
def exception_test():
    return 3/0

try:
    exception_test()
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print("AssertionError")


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

########################################################################################################################
