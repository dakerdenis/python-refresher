import math

# adius = int(input('Write circle radius'))
# 
# rea = math.pi * (radius * radius)
# 
# rea_calculated = round(area, 2)
# 
# rint(area_calculated)
# 
#----------------------------------------------------------------------------------------------

# 
# ser__name = input('Write your name: ')
# ser__lastname = input('Write your surname: ')
# 
# rint(f'{user__lastname} {user__name}')
# 
# 
#----------------------------------------------------------------------------------------------

#values = input("Input some comma separated numbers: ")
#list = values.split(",")
#tuple = tuple(list)#

#print('List: ', list)
#print('Tuple : ' , tuple)
#----------------------------------------------------------------------------------------------
#? Write a Python program that accepts a filename from the user and prints the extension of the file. Go to the editor
#? Sample filename : abc.java
#? Output : java

#file_name = input('Write your filename: ')
#
#list = file_name.split(".")
# The repr() function returns a string containing a printable representation of an object.
#
#print(repr(list[-1]))
#----------------------------------------------------------------------------------------------
#? Write a Python program to display the first and last colors from the following list. Go to the editor
#? color_list = ["Red","Green","White" ,"Black"]
# color_list = ["Red","Green","White" ,"Black"]
# 
# stalker = [color_list[0],color_list[-1]]
# print(str(stalker))
# 
#----------------------------------------------------------------------------------------------
#? 9 Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
#? exam_st_date = (11, 12, 2014)
#? Sample Output : The examination will start from : 11 / 12 / 2014
#exam_st_date = (11, 12, 2014)
#
#print("data is: %i / %i / %i/ "%exam_st_date)
#
#----------------------------------------------------------------------------------------------
#? 10  Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
#? Sample value of n is 5
#? Expected Result : 615

#def integer(value):
#    a = int(value)
#    n1 = int("%s"%a)
#    n2 = int("%s%s"%(a,a))
#    n3 = int("%s%s%s"%(a,a,a))
#    print(n1+n2+n3)
#
#integer(input("write please value"))
#

#? 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
#? Sample function : abs()
#? Expected Result :
#? abs(number) -> number
#? Return the absolute value of the argument.
# Python Docstring:
# 
# A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes the __doc__ special attribute of that object.
# 
# All modules should normally have docstrings, and all functions and classes exported by a module should also have docstrings. Public methods (including the __init__ constructor) should also have docstrings.
# 


#print(abs.__doc__)
#? 12. Write a Python program that prints the calendar for a given month and year.
#? Note : Use 'calendar' module.

# import calendar
# 
# yy = 1998
# mm = 1
# print(calendar.month(yy, mm))
# 
#? 
#? 14 Write a Python program to calculate the number of days between two dates.
#? Sample dates : (2014, 7, 2), (2014, 7, 11)
# from datetime import date
# data1 = date(1998, 1, 10)
# data2 = date(2023, 1, 20)
# 
# delta = data2 - data1
# 
# print(delta.days)

#? 15 Write a Python program to get the volume of a sphere with radius six.


# value = int(input("Write radius of sphere :" ))
# 
# rad = (4 * math.pi * (value**3))/3
# 
# print(round(rad,3))

#? 16. Write a Python program to calculate the difference between a given number and 17. 
#? If the number is greater than 17, return twice the absolute difference.
# def function(value):
#     if value > 17:
#         return (value - 17)*2
#     else:
#         return abs(value - 17) abs - return absolute value
# 
# print(function(4))
#? 17 Write a Python program to test whether a number is within 100 of 1000 or 2000
# def function(n):
#     return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
#? 19 Write a Python program to get a newly-generated string from a given string where
# ? "Is" has been added to the front. 
# ?Return the string unchanged if the given string already begins with "Is".

#def changestring(value):
#    if value [:2] == "Is":
#        return value
#    else: return "Is" + value
#
#print(changestring("Array"))
#print(changestring("IsEmpty"))
#? 20 Write a Python program that returns a string that is n 
#? (non-negative integer) copies of a given string.

# def string(value, number):
#     string=''
#     for n in range(int(number)):
#         string +=value
#     return string
# 
# print(string('suka',3))
#

#? 21 Write a Python program that determines whether a given number (accepted from the user)
#?  is even or odd, and prints an appropriate message to the user.


# num = int(input("ENter a number: "))
# if(num%2)==0:
#     print(f"{num} is Even")
# else:
#     print(f"{num} is Odd")
#? 23. Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. 
#? Return n copies of the whole string if the length is less than 2.

# def function(value, n):
#     number = abs(int(n))
#     if len(value) <= 2:
#         return value
#     else:
#         pizda = ''
#         for i in range(number):
#             pizda +=value[:2]
#         return pizda
# 
# print(function('suka yebanaya', 5))

#? 25. Write a Python program that checks whether a specified value is contained within a group of values. Go to the editor
#? Test Data :
#? 3 -> [1, 5, 8, 3] : True
#? -1 -> [1, 5, 8, 3] : False

# def checklist(value, number):
#     num = abs(int(number))
#     for x in value:
#         if x == num:
#             return True
#             break
#     return False
# 
# 
# print(checklist([1,2,3,4,5], 3))

#? 26. Write a Python program to create a histogram from a given list of integers. Go to the editor
#? Click me to see the sample solution
# def histogram(value):
#     for x in value:
#         string=''
#         for i in range(x):
#             string +='@'
#         print(string)
# 
# histogram([2, 3, 6, 5])
#? 27. Write a Python program that concatenates all elements in a list into a string and returns it
# def concat(value):
#     string=''
#     for x in value:
#         string += str(x)
#     return string
# 
# print(concat([2,3,4,5,5,56]))
#? 28. Write a Python program to print all even numbers from a given list of numbers
#?  in the same order and stop printing any after 237 in the sequence

#numbers = [    
#    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#    958,743, 527
#    ]
#
#def even_numbers(value):
#    for x in value:
#        if x == 237:
#            print(x)
#            break
#        elif x % 2 ==0:
#            print(x)
#
#
#even_numbers(numbers)


# ? 29. Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2. Go to the editor
# ? Test Data :
# ? color_list_1 = set(["White", "Black", "Red"])
# ? color_list_2 = set(["Red", "Green"])
# ? Expected Output :
# ? {'Black', 'White'}

# 
# color_list_1 = set(["White", "Black", "Red", "Green"])
# color_list_2 = set(["Red", "Green","Black","Blue","Suka"])
# 
# print("Differenct of color_list_1 and color_list_2:")
# print(color_list_1.difference(color_list_2))   #? - Выдаёт значения которых нету во втором списке
# print(color_list_2.difference(color_list_1)) #? - выдаёт значения которых нету в первом

#? 33. Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero
#numbers = [1,2,3]
#
#def sum_integers(a, b ,c):
#    sum = 0
#    if a == b or b ==c or c ==a:
#        return sum
#    else:
#        sum = a +b +c
#        return sum
#
#print(sum_integers(10,2,3))
#        

#? 34. Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
#def test(a ,b):
#    sum= 0
#    sum = a +b
#    if sum > 15 and sum < 20:
#        return 20
#    else:
#         return sum
#
#print(test(10,7))

#? 35. Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.

#! isinstance(5,int)

#def add_numbers(a, b):
#   if not (isinstance(a, int) and isinstance(b, int)):
#       return "Inputs must be integers!"
#   return a + b

#? 36 Write a Python program to add two objects if both objects are integers

#def add_objects(a,b):
#    if not(isinstance(a,int) and isinstance(b,int) ):
#        return a + b
#
#? 38. Write a Python program to solve (x + y) * (x + y).

#x, y = 4, 3
#result = x * x + 2 * x * y + y * y
#! print("({} + {}) ^ 2) = {}".format(x, y, result))


#! 41. Write a Python program to check whether a file exists.
#   import os.path
#   print(os.path.isfile('main.txt'))
#   print(os.path.isfile('main.py'))
#   import os.path
#   print(os.path.exists('main.txt'))
#   print(os.path.exists('main.py'))
#   
#   my_file = open('main.py')
#   try:
#      my_file.close()
#      print("File found!")
#   except FileNotFoundError:
#      print("File not found!")
#? 44. Write a Python program to locate Python site packages
# import site; 
# print(site.getsitepackages())


#*--------------------------------------------------------------------------

class Person:
    def __init__(self,age,weight,height,first_name,last_name, catch_phrase):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name
        self.catch_phrase = catch_phrase

user = Person(25, 80, 177, "Jon","Snow", "You know that snow")
# print(user.age)


class Robot:
    def introduce_self(self):
        print("My name is " + self.name)

r1 = Robot()
r1.name = "John"
r2 = Robot()
r2.name = "Suka"

r1.introduce_self()
r2.introduce_self()
#*--------------------------------------------------------------------------