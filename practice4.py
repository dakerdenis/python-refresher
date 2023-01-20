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

