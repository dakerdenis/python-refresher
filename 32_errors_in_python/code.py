def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Division can not be 0")    #эта ошибка идёт вместе с питоном


    return dividend / divisor


students = [
    {"name": "Bob", "grades":[75,13,14]},
    {"name": "Alex", "grades":[0]},
    {"name": "Tom", "grades":[12,14]}
]

print("Welcome to the average grade program.")

try:
    for student in students:
        name = student['name']
        grades = student['grades']        
        average = divide(sum(grades),len(grades))    
        print(f"{name}  average grade is {average}")
        
except ZeroDivisionError as e:   #it creates - variable e and put there error message
    print("there are no grades yet in your list.")    
else: 
    print(f"The average grade is {average}")
finally:
    print("Thank you!")

    

 