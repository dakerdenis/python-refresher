# users = [
#     (0, "Bob", "password"),
#     (1, "Rolf", "bob123"),
#     (2, "Jose", "longp4assword"),
#     (3, "username", "1234"),
# ]
# 
# username_mapping = {user[1]: user for user in users} #!--user[1]: user - ключевое значения для поиска по имени поскольку user[1] - это имя
# 
# username_input = input("Enter your username: ")
# password_input = input("Enter your password: ")
# 
# _,username, password = username_mapping[username_input] #!---- _  this symbol means that this key не считается и не уитывается
# 
# if password_input == password:
#     print("Your details are correct")
# else:
#     print("Incorrect data")
# 



















# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {"name": "Jose", "school": "Computing", "grades": (66,77,88)}

# Assume the argument, data, is a dictionary.

# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades = data['grades']  
    return sum(grades) / len(grades)


# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total = total + sum(student['grades'])
        count = count + len(student['grades'])

    return total / count