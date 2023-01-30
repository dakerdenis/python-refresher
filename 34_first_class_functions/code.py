def devide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Division cannot be 0.")
    return dividend / divisor

def calculate (*values, operator):       # *values - collect values and put them into toples
    return operator(*values)

result = calculate(2,4 , operator=devide)   # function - here could be variable 












def search(sequence, expected,finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")

friends = [
    {"name": "Adolf Smith", "age": 24},
    {"name": "Dolf Lungden", "age": 35},
    {"name": "Arnold Schwarzeneger", "age": 29}
]


def get_frined_name(friend):
    return friend["name"]

expected_value = "Bob Smith"

result = search(friends,expected_value,get_frined_name)

print(result)