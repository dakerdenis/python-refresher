def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Division")    #эта ошибка идёт вместе с питоном

    return dividend / divisor


grades = []

print("Welcome to the average grade program.")
if len(grades) == 0:
    print("You don't have grades")    
average = divide(sum(grades),len(grades))

print(f"Average marks: {average}")