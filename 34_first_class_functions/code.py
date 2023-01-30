def devide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Division cannot be 0.")
    return dividend / divisor

def calculate (*values, operator):       # *values - collect values and put them into toples
    return operator(*values)

result = calculate(2,4 , operator=devide)

print(result)