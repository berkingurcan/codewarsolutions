#!/usr/bin/env python
# coding: utf-8

# # My Codewars Solutions on Python 8-7-6-5 Kyu Problems
# ### Also includes a little bit 7-8 Kyu C++, SQL and Haskell solutions

# #Find the missing letter
# 
# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
# 
# You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
# The array will always contain letters in only one case.
# 
# Example:
# 
# ['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'
# 
# ["a","b","c","d","f"] -> "e"
# ["O","Q","R","S"] -> "P"
# (Use the English alphabet with 26 letters!)
# 
# Have fun coding it and please don't forget to vote and rank this kata! :-)
# 
# I have also created other katas. Take a look if you enjoyed this kata!
# 
# https://www.codewars.com/kata/5839edaa6754d6fec10000a2

# In[5]:


def find_missing_letter(chars):
    alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    a = chars[0]
    b = chars[-1]
    listo = alphas[alphas.index(a):alphas.index(b)]
    
    return "".join(set(listo) - set(chars))


# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.
# 
# For example:
# 
# uniqueInOrder('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# uniqueInOrder('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# uniqueInOrder([1,2,2,3,3])       == [1,2,3]
# 
# https://www.codewars.com/kata/54e6533c92449cc251001667

# In[6]:


def unique_in_order(iterable):
    if len(iterable) > 0:
        listt = [iterable[0]]
        for i in range(1,len(iterable)):
            if iterable[i-1] == iterable[i]:
                pass
            else:
                listt.append(iterable[i])
        return listt
    else:
        return []


# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
# 
# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 
# Notes
# 
# Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!
# 
# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

# In[7]:


def duplicate_encode(word):
    word = word.lower()
    w = ""
    for i in word:
        if word.count(i) > 1:
            w += ")"
        else:
            w += "("
    return w


# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
# 
# Example:
# createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parentheses!
# 
# https://www.codewars.com/kata/525f50e3b73515a6db000b83

# In[8]:


def create_phone_number(n):
    no = "("
    for i in range(3):
        no += str(n[i])
    no = no + ") "
    for t in range(3,6):
        no += str(n[t])
    no = no + "-"
    for u in range(6,10):
        no += str(n[u])
    return no


# You are given an odd-length array of integers, in which all of them are the same, except for one single number.
# 
# Complete the method which accepts such an array, and returns that single different number.
# 
# The input array will always be valid! (odd-length >= 3)
# 
# Examples
# [1, 1, 2] ==> 2
# [17, 17, 3, 17, 17, 17, 17] ==> 3
# 
# https://www.codewars.com/kata/57f609022f4d534f05000024

# HASKELL
# 
# A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?
# 
# Return True if yes, False otherwise :)

# In[12]:



# module Survive where

# hero :: Int -> Int -> Bool
# hero x y = if (x >= 2*y) then True else False


# C++ 
# 
# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

# In[13]:


# int simpleMultiplication(int a){
#    if (a % 2 == 0) {
#      return a*8;
#      }
#    else {
#     return a*9;
#    }
# }


# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
# 
# Examples:
# 
# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
# 
# spinWords( "This is a test") => returns "This is a test"
# 
# spinWords( "This is another test" )=> returns "This is rehtona test"
# 
# https://www.codewars.com/kata/5264d2b162488dc400000001

# In[14]:


def spin_words(sentence):
    x = sentence.split()
    y = []
    for i in x:
        if len(i) > 4:
            i = i[::-1]
            y.append(i)
        else:
            y.append(i)
    return "".join(t + " " for t in y).rstrip()


# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!
# 
# Here's the deal:
# 
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
# Examples
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false
# 
# https://www.codewars.com/kata/52449b062fb80683ec000024

# In[15]:


def generate_hashtag(s):
    s = s.split()
    y = []
    for i in s:
        y.append(i.capitalize())
    x = '#'
    for t in y:
        x += t
    if len(x) > 140:
        return False
    if len(x) < 1:
        return False
    if x == "#":
        return False
    else:
        return x


# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
# 
# Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:
# 
# likes [] -- must be "no one likes this"
# likes ["Peter"] -- must be "Peter likes this"
# likes ["Jacob", "Alex"] -- must be "Jacob and Alex like this"
# likes ["Max", "John", "Mark"] -- must be "Max, John and Mark like this"
# likes ["Alex", "Jacob", "Mark", "Max"] -- must be "Alex, Jacob and 2 others like this"
# 
# https://www.codewars.com/kata/5266876b8f4bf2da9b000362

# In[16]:


def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif len(names) >= 4:
        return f"{names[0]}, {names[1]} and {len(names)-2} others like this"


# https://www.codewars.com/kata/5526fc09a1bbd946250002dc
#     
# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
# 
# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)
# 
# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)

# In[17]:


def find_outlier(integers):
    cift = []
    tek = []
    for i in integers:
        if i % 2 == 0:
            cift.append(i)
        else:
            tek.append(i)
    if len(cift) == 1:
        return cift[0]
    else:
        return tek[0]


# https://www.codewars.com/kata/54da5a58ea159efa38000836
#     
# Given an array of integers, find the one that appears an odd number of times.
# 
# There will always be only one integer that appears an odd number of times.

# In[18]:


def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 == 1:
            return i
        else:
            continue


# https://www.codewars.com/kata/55c1d030da313ed05100005d
# 
# Now that we have a Block let's move on to something slightly more complex a Sphere.
# 
# #Arguments for the constructor
# 
# radius -> integer or float (do not round it)
# mass -> integer or float (do not round it)
# #Methods to be defined
# 
# get_radius()       =>  radius of the Sphere (do not round it)
# get_mass()         =>  mass of the Sphere (do not round it)
# get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
# get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
# get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)
# ##Example
# 
# ball = Sphere(2,50)
# ball.get_radius() ->       2
# ball.get_mass() ->         50
# ball.get_volume() ->       33.51032
# ball.get_surface_area() -> 50.26548
# ball.get_density() ->      1.49208

# In[19]:


import math 
import decimal
class Sphere(object):
    def __init__(self,radius,mass):
        self.radius = radius
        self.mass = mass
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_volume(self):
        return round(float(4/3 * (math.pi * (self.radius**3))),5)
    def get_surface_area(self):
        return round(float(4*(math.pi * (self.radius**2))),5)
    def get_density(self):
        return round(float(self.get_mass()/self.get_volume()),5)


# The following code was thought to be working properly, however when the code tries to access the age of the person instance it fails.
# 
# person = Person.new('Yukihiro', 'Matsumoto', 47)
# puts person.full_name
# puts person.age
# For this exercise you need to fix the code so that it works correctly.
# 
# https://www.codewars.com/kata/513f887e484edf3eb3000001

# In[20]:


class Person():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = f"{first_name} {last_name}"


# Write a function sum that accepts an unlimited number of integer arguments, and adds all of them together.
# 
# The function should reject any arguments that are not integers, and sum the remaining integers.
# 
# sum(1, 2, 3)   // -> 6
# sum(1, "2", 3) // -> 4
# 
# https://www.codewars.com/kata/536c738e49aa8b663b000301

# In[21]:


def sum(*args):
    x = 0
    for i in args:
        if type(i) == int:
            x += i
    return x


# https://www.codewars.com/kata/56cd44e1aa4ac7879200010b
# 
# Is the string uppercase?
# Task
# Add the isUpperCase method to String to see whether the string is ALL CAPS. For example:
# 
# "c".isUpperCase() == false
# "C".isUpperCase() == true
# "hello I AM DONALD".isUpperCase() == false
# "HELLO I AM DONALD".isUpperCase() == true
# "ACSKLDFJSgSKLDFJSKLDFJ".isUpperCase() == false
# "ACSKLDFJSGSKLDFJSKLDFJ".isUpperCase() == true
# In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter so any string containing no letters at all is trivially considered to be in ALL CAPS

# In[22]:


def is_uppercase(inp):
    return inp.isupper()


# https://www.codewars.com/kata/547274e24481cfc469000416
# 
# According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.
# 
# You have to do God's job. The creation method must return an array of length 2 containing objects (representing Adam and Eve). The first object in the array should be an instance of the class Man. The second should be an instance of the class Woman. Both objects have to be subclasses of Human. Your job is to implement the Human, Man and Woman classes.

# In[23]:


class Human():
    pass

class Man(Human):
    pass

class Woman(Human):
    pass



def God():
    return [Man(),Woman()]


# https://www.codewars.com/kata/55a144eff5124e546400005a
#     
# Basic Classes, this kata is mainly aimed at the new JS ES6 Update introducing classes
# Task
# Your task is to complete this Class, the Person class has been created. You must fill in the Constructor method to accept a name as string and an age as number, complete the get Info property and getInfo method/Info getter which should return johns age is 34

# In[24]:


class Person:
    def __init__(self,name,age):
        self.info = f"{name}s age is {age}"


# https://www.codewars.com/kata/55a14aa4817efe41c20000bc
# 
# Classy Extensions, this kata is mainly aimed at the new JS ES6 Update introducing extends keyword. You will be preloaded with the Animal class, so you should only edit the Cat class.
# Task
# Your task is to complete the Cat class which Extends Animal and replace the speak method to return the cats name + meows. e.g. 'Mr Whiskers meows.'
# The name attribute is passed with this.name (JS), @name (Ruby) or self.name (Python).

# In[26]:


class Cat(Animal):
    def __init__(self,name):
        self.name=name
    def speak(self):
        return(f'{self.name} meows.')


# https://www.codewars.com/kata/53f0f358b9cb376eca001079
#     
#     Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
# 
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
# 
# ball1 = new Ball();
# ball2 = new Ball("super");
# 
# ball1.ballType     //=> "regular"
# ball2.ballType     //=> "super"

# In[27]:


class Ball(object):
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type


# https://www.codewars.com/kata/55849d76acd73f6cc4000087
# 
# Let's imagine we have a popular online RPG. A player begins with a score of 0 in class E5. A1 is the highest level a player can achieve.
# 
# Now let's say the players wants to rank up to class E4. To do so the player needs to achieve at least 100 points to enter the qualifying stage.
# 
# Write a script that will check to see if the player has achieved at least 100 points in his class. If so, he enters the qualifying stage.
# 
# In that case, we return, "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up.".
# 
# Otherwise return, False/false (according to the language n use).

# In[28]:


def playerRankUp(pts):
    if pts >= 100:
        return "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up."
    else:
        return False


# https://www.codewars.com/kata/53f1015fa9fe02cbda00111a
# 
# Create a class Ghost
# 
# Ghost objects are instantiated without any arguments.
# 
# Ghost objects are given a random color attribute of white" or "yellow" or "purple" or "red" when instantiated

# In[29]:


import random
class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white","yellow","purple","red"])


# 
# https://www.codewars.com/kata/53cf459503f9bbb774000003
# 
# Python is now supported on Codewars!
# 
# For those of us who are not very familiar with Python, let's handle the very basic challenge of creating a class named Python. We want to give our Pythons a name, so it should take a name argument that we can retrieve later.

# In[30]:


class Python:
    def __init__(self,name):
        self.name = name


# https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9
# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
# 
# Write a function which takes a list of strings and returns each line prepended by the correct number.
# 
# The numbering starts at 1. The format is n: string. Notice the colon and space in between.
# 
# Examples:
# 
# number([]) // => []
# number(["a", "b", "c"]) // => ["1: a", "2: b", "3: c"]

# In[31]:


def number(lines):
    lines.insert(0, "HEHE")
    list = []
    for i,y in enumerate(lines):
        list.append(str(i)+": "+y)
    del list[0]
    return list


# https://www.codewars.com/kata/5ebd53ea50d0680031190b96
#     
#     Your Task
# Complete the function to convert an integer into a string of the Turkish name.
# 
# input will always be an integer 0-99;
# output should always be lower case.
# Background
# Forming the Turkish names for the numbers 0-99 is very straightforward:
# 
# units (0-9) and tens (10, 20, 30, etc.) each have their own unique name;
# all other numbers are simply [tens] + [unit], like twenty one in English.
# Unlike English, Turkish does not have "teen"-suffixed numbers; e.g. 13 would be directly translated as "ten three" rather than "thirteen" in English.
# 
# Turkish names of units and tens are as follows:
# 
# 0 = sıfır
# 1 = bir
# 2 = iki
# 3 = üç
# 4 = dört
# 5 = beş
# 6 = altı
# 7 = yedi
# 8 = sekiz
# 9 = dokuz
# 
# 10 = on
# 20 = yirmi
# 30 = otuz
# 40 = kırk
# 50 = elli
# 60 = altmış
# 70 = yetmiş
# 80 = seksen
# 90 = doksan
# Examples

# In[32]:


def get_turkish_number(num):
#selamlar :)))
    birler = {1: " bir",
            2: " iki",
            3: " üç",
            4:" dört",
            5:" beş",
            6:" altı",
            7:" yedi",
            8:" sekiz",
            9:" dokuz",
             0:""}
    onlar = {1:"on",
            2:"yirmi",
            3:"otuz",
            4:"kırk",
            5:"elli",
            6:"altmış",
            7:"yetmiş",
            8:"seksen",
            9:"doksan",
            }
    x = num // 10
    y = num % 10
    if num > 9:
        return onlar[x]+birler[y]
    if num == 0:
        return "sıfır"
    else:
        return birler[num].replace(" ","")


# https://www.codewars.com/kata/5a2b703dc5e2845c0900005a
#     
#     Your task is to create functionisDivideBy (or is_divide_by) to check if an integer number is divisible by each out of two arguments.
# 
# A few cases:
# 
# 
# (-12, 2, -6)  ->  true
# (-12, 2, -5)  ->  false
# 
# (45, 1, 6)    ->  false
# (45, 5, 15)   ->  true
# 
# (4, 1, 4)     ->  true
# (15, -5, 3)   ->  true

# In[33]:


def is_divide_by(number, a, b):
    return True if number % a == 0 and number % b == 0 else False


# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# 
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# 
# Note: If the number is a multiple of both 3 and 5, only count it once. Also, if a number is negative, return 0(for languages that do have them

# In[34]:


def solution(number):
    x = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            x.append(i)
    return sum(x)


# https://www.codewars.com/kata/5545f109004975ea66000086
# 
# Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero digits.
# 
# Examples:
# 1) n =   3, x = 1, y = 3 =>  true because   3 is divisible by 1 and 3
# 2) n =  12, x = 2, y = 6 =>  true because  12 is divisible by 2 and 6
# 3) n = 100, x = 5, y = 3 => false because 100 is not divisible by 3
# 4) n =  12, x = 7, y = 5 => false because  12 is neither divisible by 7 nor 5

# In[35]:


def is_divisible(n,x,y):
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False


# Your task is to remove all duplicate words from a string, leaving only single (first) words entries.
# 
# Example:
# 
# Input:
# 
# 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
# 
# Output:
# 
# 'alpha beta gamma delta'
# 
# https://www.codewars.com/kata/5b39e3772ae7545f650000fc

# In[36]:


def remove_duplicate_words(s):
    x = []
    u = s.split()
    for i in u:
        if i not in x:
            x.append(i)
    return "".join(t + " " for t in x).rstrip()


# https://www.codewars.com/kata/52fba66badcd10859f00097e
# 
# Trolls are attacking your comment section!
# 
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# 
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# 
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# 
# Note: for this kata y isn't considered a vowel.

# In[37]:


import re
def disemvowel(string):
    n = re.findall("[aeıioöuüAEIİOÖUÜ]",string)
    vv = []
    for i in string:
        if i not in n:
            vv.append(i)
    return "".join(i for i in vv)


# Normally we have firstname, middle and the last name but there may be more than one word in a name like a South Indian one.
# 
# Similar to those kinda names we need to initialize the names.
# 
# See the pattern below:
# 
# initials('code wars') => returns C.Wars 
# initials('Barack Hussain obama') => returns B.H.Obama 
# 
# 
# https://www.codewars.com/kata/55968ab32cf633c3f8000008

# In[40]:


def initials(name):
    x = name.title().split()
    y = []
    for i in x:
        y.append(i[0]+".")
    y[-1] = x[-1]
    return "".join(i for i in y)


# Your task is simply to count the total number of lowercase letters in a string.
# https://www.codewars.com/kata/56a946cd7bd95ccab2000055

# In[41]:


import re
def lowercase_count(strng):
    return len(re.findall("[a-z]",strng))


# https://www.codewars.com/kata/56a25ba95df27b7743000016
#     Basic regex tasks. Write a function that takes in a numeric code of any length. The function should check if the code begins with 1, 2, or 3 and return true if so. Return false otherwise.
# 
# You can assume the input will always be a number.

# In[42]:


import re
def validate_code(code):
    return bool(re.match("^1|2|3",str(code)))


# https://www.codewars.com/kata/593c9175933500f33400003e
# 
# 
# Implement a function, multiples(m, n), which returns an array of the first m multiples of the real number n. Assume that m is a positive integer.
# 
# Ex.
# 
# multiples(3, 5.0)
# should return
# 
# [5.0, 10.0, 15.0]

# In[43]:


def multiples(m, n):
    x = []
    for i in range(1,m+1):
        x.append(n * i)
    return x


# https://www.codewars.com/kata/5897cdc26551af891c000124
# 
# Hofstadter sequences are a family of related integer sequences, among which the first ones were described by an American professor Douglas Hofstadter in his book Gödel, Escher, Bach.
# 
# Task
# Today we will be implementing the rather chaotic recursive sequence of integers called Hofstadter Q.
# 
# The Hofstadter Q is defined as:
# 
# 
# As the author states in the aforementioned book:
# 
# 
# It is reminiscent of the Fibonacci definition in that each new value is a sum of two previous values-but not of the immediately previous two values. Instead, the two immediately previous values tell how far to count back to obtain the numbers to be added to make the new value.
# The function produces the starting sequence:
# 1, 1, 2, 3, 3, 4, 5, 5, 6 . . .
# Test info: 100 random tests, n is always positive

# In[44]:


x = []
for i in range(10000):
    x.append(0)
x[0] = 1
x[1] = 1
x[2] = 1
def hofstadter_Q(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        if x[n] != 0:
            return x[n]
        if x[n] == 0:
            x[n] = hofstadter_Q(n -  hofstadter_Q(n-1)) +  hofstadter_Q(n - hofstadter_Q(n-2))
            return x[n]


# https://www.codewars.com/kata/579637b41ace7f92ae000282
#     
#     What is a Catalan number?
# In combinatorial mathematics, the Catalan numbers form a sequence of natural numbers that occur in various counting problems, often involving recursively-defined objects. They are named after the Belgian mathematician Eugène Charles Catalan (1814–1894).
# 
# Using zero-based numbering, the nth Catalan number is given directly in terms of binomial coefficients by:
# 
# 
# You can read more on Catalan numbers Here.
# 
# Task:
# Implement a function which calculates the Nth Catalan number.
# 
# 0  =>  1
# 3  =>  5
# 7  =>  429
# 9  =>  4862
# Hint: avoid the use of floats
# 
# Have fun :)

# In[45]:


import math
def nth_catalan_number(n):
    n = int(n)
    if n == 0:
        return 1
    else:
        x = ((math.factorial(2*int(n))) // (math.factorial(int(n))* (math.factorial(int(n))))) // (int(n+1))
        return int(x)


# https://www.codewars.com/kata/59e19a747905df23cb000024
#     
#     
#     Take an input string and return a string that is made up of the number of occurences of each english letter in the input followed by that letter, sorted alphabetically. The output string shouldn't contain chars missing from input (chars with 0 occurence); leave them out.
# 
# An empty string, or one with no letters, should return an empty string.
# 
# Notes:
# 
# the input will always be valid;
# treat letters as case-insensitive
# Examples
# "This is a test sentence."  ==>  "1a1c4e1h2i2n4s4t"
# ""                          ==>  ""
# "555"                       ==>  ""

# In[46]:


def string_letter_count(s):
    a = []
    for i in s.lower():
        if i.isalpha():
            a.append(i)
    e = list(dict.fromkeys(a))
    return "".join(str(a.count(t)) + t for t in sorted(e))


# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
# 
# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
# 
# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice

# In[47]:


def duplicate_count(text):
    x = []
    t2 = text.lower()
    for i in t2:
        if t2.count(i) > 1:
            x.append(i)
    x = list(dict.fromkeys(x))
    return len(x)


# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4
# 
# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
# 
# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

# In[48]:


def reverse_words(text):
    return "".join(i[::-1] + " " for i in text.split(" ")).rstrip()


# https://www.codewars.com/kata/52a112d9488f506ae7000b95
#     
#     Write a function with the signature shown below:
# 
# function isIntArray(arr) {
#   return true
# }
# returns true / True if every element in an array is an integer or a float with no decimals.
# returns true / True if array is empty.
# returns false / False for every other input.

# In[49]:


def is_int_array(arr):
    if arr is None:
        return False
    elif arr is "":
        return False
    else:
        for i in arr:
            if i == "":
                return False
            elif isinstance(i, int):
                continue
            elif type(i) is float and i % 1 == 0:
                continue
            else:
                return False
        return True


# https://www.codewars.com/kata/523f5d21c841566fde000009
# 
# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
# 
# It should remove all values from list a, which are present in list b.
# 
# arrayDiff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
# 
# arrayDiff([1,2,2,2,3],[2]) == [1,3]

# In[50]:


def array_diff(a, b):
    x = []
    for i in a:
        if i not in b:
            x.append(i)
    return x


# https://www.codewars.com/kata/5270d0d18625160ada0000e4
#     
#     Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.
# 
#  Three 1's => 1000 points
#  Three 6's =>  600 points
#  Three 5's =>  500 points
#  Three 4's =>  400 points
#  Three 3's =>  300 points
#  Three 2's =>  200 points
#  One   1   =>  100 points
#  One   5   =>   50 point
# A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.
# 
# Example scoring
# 
#  Throw       Score
#  ---------   ------------------
#  5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
#  1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
#  2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
# In some languages, it is possible to mutate the input to the function. This is something that you should never do. If you mutate the input, you will not be able to pass all the tests.

# In[51]:


def score(dice):
    a = dice.count(1)
    b = dice.count(6)
    c = dice.count(5)
    d = dice.count(4)
    e = dice.count(3)
    f = dice.count(2)
    if a >= 3:
        return 1000 + (a-3)*100 + c*50
    elif b >= 3:
        return 600 + a*100 + c*50
    elif c >= 3:
        return 500 + a*100 + (c-3)*50
    elif d >= 3:
        return 400 + a*100 + c*50
    elif e >= 3:
        return 300 + a*100 + c*50
    elif f >= 3:
        return 200 + a*100 + c*50
    else:
        return a*100 + c*50


# https://www.codewars.com/kata/54da539698b8a2ad76000228
# 
# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.
# 
# Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).

# In[52]:


def is_valid_walk(walk):
    w = walk.count("w")
    e = walk.count("e")
    s = walk.count("s")
    n = walk.count("n")
    if w + e + s + n == 10:
        if w == e and n == s:
            return True
        else:
            return False
    else:
        return False


# https://www.codewars.com/kata/589631d24a7323d18d00016f
#     
#     You're continuing to enjoy your new piano, as described in Piano Kata, Part 1. You're also continuing the exercise where you start on the very first (leftmost, lowest in pitch) key on the 88-key keyboard, which (as shown below) is the note A, with the little finger on your left hand, then the second key, which is the black key A# ("A sharp"), with your left ring finger, then the third key, B, with your left middle finger, then the fourth key, C, with your left index finger, and then the fifth key, C#, with your left thumb. Then you play the sixth key, D, with your right thumb, and continue on playing the seventh, eighth, ninth, and tenth keys with the other four fingers of your right hand. Then for the eleventh key you go back to your left little finger, and so on. Once you get to the rightmost/highest, 88th, key, C, you start all over again with your left little finger on the first key.
# 
# 
# 
# (If the Codewars Instructions pane resizes the above piano keyboard image to be too small to read the note labels of the black/sharp keys on your screen, click here to open a copy of the image in a new tab or window.)
# 
# This time, in addition to counting each key press out loud (not starting again at 1 after 88, but continuing on to 89 and so forth) to try to keep a steady rhythm going and to see how far you can get before messing up, you're also saying the name of each note. You wonder whether this may help you develop perfect pitch in addition to learning to just know which note is which, and -- as in Piano Kata, Part 1 -- helping you to learn to move smoothly and with uniform pressure on the keys from each finger to the next and back and forth between hands.
# 
# The function you are going to write will explore one of the patterns you're experiencing in your practice: Given the number you stopped on, which note was it? For example, in the description of your piano exercise above, if you stopped at 5, your left thumb would be on the fifth key of the piano, which is C#. Or if you stopped at 92, you would have gone all the way from keys 1 to 88 and then wrapped around, so that you would be on the fourth key, which is C.
# 
# Your function will receive an integer between 1 and 10000 (maybe you think that in principle it would be cool to count up to, say, a billion, but considering how many years it would take it is just not possible) and return one of the strings "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", or "G#" indicating which note you stopped on -- here are a few more examples:
# 
# 1     "A"
# 12    "G#"
# 42    "D"
# 100   "G#"
# 2017  "F"

# In[53]:


def which_note(key_press_count):
    n = ["G#","A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G"]
    if key_press_count % 88 == 0:
        return "C"
    else:
        return n[(key_press_count % 88 % 12)]


# https://www.codewars.com/kata/545cedaa9943f7fe7b000048
#     
#     A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
# 
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

# In[54]:


import string
def is_pangram(s):
    a = "abcdefghijklmnopqrstuvwxyz"
    for i in a:
        if i in s.lower():
            continue
        else:
            return False
    return True


# https://www.codewars.com/kata/526dbd6c8c0eb53254000110
# 
# In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None, so you don't have to check that.
# 
# The string has the following conditions to be alphanumeric:
# 
# At least one character ("" is not valid)
# Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
# No whitespaces / underscore

# In[55]:


def alphanumeric(password):
    n = []
    if password == "":
        return False
    for i in password:
        if i.isdigit() or i.isalpha():
            n.append(i)
        else:
            return False
    if ("".join(n)) == password:
        return True


# https://www.codewars.com/kata/5511b2f550906349a70004e1
# 
# Define a function that takes in two non-negative integers aaa and bbb and returns the last decimal digit of aba^ba 
# b
#  . Note that aaa and bbb may be very large!
# 
# For example, the last decimal digit of 979^79 
# 7
#   is 999, since 97=47829699^7 = 47829699 
# 7
#  =4782969. The last decimal digit of (2200)2300({2^{200}})^{2^{300}}(2 
# 200
#  ) 
# 2 
# 300
#  
#  , which has over 109210^{92}10 
# 92
#   decimal digits, is 666. Also, please take 000^00 
# 0
#   to be 111.
# 
# You may assume that the input will always be valid.

# In[57]:


def last_digit(n1, n2):
    if n2 == 0:
        return 1
    elif int(str(n1)[-1]) == 1:
        return 1
    elif int(str(n1)[-1]) == 2:
        if n2 % 4 == 1:
            return 2
        elif n2 % 4 == 2:
            return 4
        elif n2 % 4 == 3:
            return 8
        elif n2 % 4 == 0:
            return 6
    elif int(str(n1)[-1]) == 3:
        if n2 % 4 == 1:
            return 3
        elif n2 % 4 == 2:
            return 9
        elif n2 % 4 == 3:
            return 7
        else:
            return 1
    elif int(str(n1)[-1]) == 4:
        if n2 % 2 == 1:
            return 4
        else:
            return 6
    elif int(str(n1)[-1]) == 5:
        return 5
    elif int(str(n1)[-1]) == 6:
        return 6
    elif int(str(n1)[-1]) == 7:
        if n2 % 4 == 1:
            return 7
        elif n2 % 4 == 2:
            return 9
        elif n2 % 4 == 3:
            return 3
        else:
            return 1
    elif int(str(n1)[-1]) == 8:
        if n2 % 4 == 1:
            return 8
        elif n2 % 4 == 2:
            return 4
        elif n2 % 4 == 3:
            return 2
        else:
            return 6
    elif int(str(n1)[-1]) == 9:
          if n2 % 2 == 1:
              return 9
          else:
              return 1
    elif int(str(n1)[-1]) == 0:
        return 0


# https://www.codewars.com/kata/530e15517bc88ac656000716
# 
# 
# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
# 
# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# In[58]:


def rot13(message):
    kn = list("abcdefghijklmnopqrstuvwxyz")
    k13 = list("nopqrstuvwxyzabcdefghijklm")
    bn = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    b13 = list("NOPQRSTUVWXYZABCDEFGHIJKLM")
    conc = []
    for i in message:
        if i.islower():
            conc.append(k13[kn.index(i)])
        elif i.isupper():
            conc.append(b13[bn.index(i)])
        else:
            conc.append(i)
    return "".join(conc)


# https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8
# 
# The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.
# 
# Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
# 
# Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?
# 
# Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.

# In[59]:


def tickets(people):
    x = []
    for i in people:
        if i == 25:
            x.append(25)
        elif i == 50:
            if 25 in x:
                x.append(50)
                x.remove(25)
            else:
                return "NO"
        else:
            if 25 in x and 50 in x:
                x.remove(50)
                x.remove(25)
            elif x.count(25) > 2:
                x.remove(25)
                x.remove(25)
                x.remove(25)
            else: 
                return "NO" 
    return "YES"


# https://www.codewars.com/kata/54c2fc0552791928c9000517
# 
# Write this function
# 
# 
# for i from 1 to n, do i % m and return the sum
# 
# f(n=10, m=5) // returns 20 (1+2+3+4+0 + 1+2+3+4+0)
# You'll need to get a little clever with performance, since n can be a very large number

# In[60]:


def f(n, m):
    if n % m == 0:
        return (n/m)*(((m-1) * m) / 2)
    else:
        return int(n/m)*(((m-1) * m) / 2) + ((n - int(n/m)*m) * ((n - int(n/m)*m)+1)) / 2
    
    #15 10:  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15


# https://www.codewars.com/kata/54df2067ecaa226eca000229
# 
# Due to another of his misbehaved, the primary school's teacher of the young Gauß, Herr J.G. Büttner, to keep the bored and unruly young schoolboy Karl Friedrich Gauss busy for a good long time, while he teaching arithmetic to his mates, assigned him the problem of adding up all the whole numbers from 1 through a given number n.
# 
# Your task is to help the young Carl Friedrich to solve this problem as quickly as you can; so, he can astonish his teacher and rescue his recreation interval.
# 
# Here's, an example:
# 
# f(n=100) // returns 5050 
# It's your duty to verify that n is a valid positive integer number. If not, please, return false (None for Python, null for C#).
# 
# Note: the goal of this kata is to invite you to think about some 'basic' mathematic formula and how you can do performance optimization on your code. 
# 
# Advanced - experienced users should try to solve it in one line, without loops, or optimizing the code as much as they can.
# 
# 

# In[61]:


def f(n):
    if type(n) == int and n > 0:
        return (n * (n + 1)) / 2
    else:
        return None


# https://www.codewars.com/kata/5287e858c6b5a9678200083c
# 
# A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).
# 
# For example, take 153 (3 digits), which is narcisstic:
# 
#     1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# and 1652 (4 digits), which isn't:
# 
#     1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
# The Challenge:
# 
# Your code must return true or false depending upon whether the given number is a Narcissistic number in base 10.
# 
# Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.

# In[62]:


def narcissistic(value):
    x = sum(int(i) ** len(str(value)) for i in str(value))
    if x == value:
        return True
    else:
        return False


# https://www.codewars.com/kata/52685f7382004e774f0001f7
# 
# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
# 
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)
# 
# You can find some examples in the test fixtures.

# In[63]:


def make_readable(seconds):
    x = int(seconds / 3600)
    y = int((seconds - x * 3600) / 60)
    z = int((seconds - x * 3600) - y * 60)
    if x < 10:
        x = "0" + str(x)  
    if y < 10:
        y = "0" + str(y) 
    if z < 10:
        z = "0" + str(z)    
    return str(x) + ":" + str(y) + ":" + str(z)


# https://www.codewars.com/kata/54ff3102c1bad923760001f3
# 
# 
# Return the number (count) of vowels in the given string.
# 
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# 
# The input string will only consist of lower case letters and/or spaces.

# https://www.codewars.com/kata/551dc350bf4e526099000ae5
# 
# Polycarpus works as a DJ in the best Berland nightclub, and he often uses dubstep music in his performance. Recently, he has decided to take a couple of old songs and make dubstep remixes from them.
# 
# Let's assume that a song consists of some number of words (that don't contain WUB). To make the dubstep remix of this song, Polycarpus inserts a certain number of words "WUB" before the first word of the song (the number may be zero), after the last word (the number may be zero), and between words (at least one between any pair of neighbouring words), and then the boy glues together all the words, including "WUB", in one string and plays the song at the club.
# 
# For example, a song with words "I AM X" can transform into a dubstep remix as "WUBWUBIWUBAMWUBWUBX" and cannot transform into "WUBWUBIAMWUBX".
# 
# Recently, Jonny has heard Polycarpus's new dubstep track, but since he isn't into modern music, he decided to find out what was the initial song that Polycarpus remixed. Help Jonny restore the original song.
# 
# Input
# The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length doesn't exceed 200 characters
# 
# Output
# Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.
# 
# Examples
# songDecoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
#   // =>  WE ARE THE CHAMPIONS MY FRIEND

# In[64]:


def song_decoder(song):
    song = song.replace("WUB", " ")
    song = " ".join(song.split())
    return song


# There is an array with some numbers. All numbers are equal except for one. Try to find it!
# 
# findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
# findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
# It’s guaranteed that array contains at least 3 numbers.
# 
# The tests contain some very huge arrays, so think about performance.
# 
# https://www.codewars.com/kata/585d7d5adb20cf33cb000235

# In[65]:


def find_uniq(arr):
    arr == arr.sort()
    y = len(arr)
    if arr[0] != arr[1]:
        n = arr[0]
    else:
        n = arr[y - 1]
    return n   # n: unique integer in the array


# https://www.codewars.com/kata/583f158ea20cfcbeb400000a
# 
# Given two numbers and an arithmetic operator (the name of it, as a string), return the result of the two numbers having that operator used on them.
# 
# a and b will both be positive integers, and a will always be the first number in the operation, and b always the second.
# 
# The four operators are "add", "subtract", "divide", "multiply".
# 
# 

# In[66]:


def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    else:
        return a/b


# https://www.codewars.com/kata/57f36495c0bb25ecf50000e7
#     
#     Your task is to write function findSum.
# 
# Upto and including n, this function will return the sum of all multiples of 3 and 5.
# 
# For example:
# 
# findSum(5) should return 8 (3 + 5)
# 
# findSum(10) should return 33 (3 + 5 + 6 + 9 + 10)

# In[67]:


def find(n):
    return sum(i for i in range(0,n+1) if i % 3 == 0 or i % 5 == 0)


# https://www.codewars.com/kata/587731fda577b3d1b0001196
# 
# Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. All words must have their first letter capitalized without spaces.
# 
# For instance:
# 
# "hello case".camelCase() => HelloCase
# "camel case word".camelCase() => CamelCaseWord
# Don't forget to rate this kata! Thanks :)

# In[68]:


def camel_case(string):
    return string.title().replace(" ", "")


# https://www.codewars.com/kata/5556282156230d0e5e000089
# 
# Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').
# 
# Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').
# 
# Create a function which translates a given DNA string into RNA.

# In[69]:


def dna_to_rna(dna):
    return dna.replace("T","U")
    


# https://www.codewars.com/kata/55685cd7ad70877c23000102
# 
# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

# In[70]:


def make_negative( number ):
    if number > 0:
        return number - 2 * number
    else: 
        return number


# In[ ]:




