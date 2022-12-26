numbers = [1, 3, 5]
doubled = [nume * 2 for nume in numbers]

friends = ["Rolf", "Sam", "Samantha", "Suka", "Jen"]
starts_s = [f for f in friends if f.startswith("S")]


workes = [
    {"name": "Denis", "salary": 2000},
    {"name": "Eblan", "salary": 1500},
    {"name": "Sabit", "salary": 3000},
]
 
#print(workes[1]["salary"])

student__attendance = {
    "Rolf": 96,
    "Bob": 80,
    "Anne": 100
}

#for student, attendance in student__attendance.items(): #! Items() access for both values
#    print(f"{student}: {attendance}")
print(list(student__attendance.items()))
for t in student__attendance.items():
    print(t)
#attendance__values = student__attendance.items()

#print(sum(attendance__values)/len(attendance__values))
print("----------------Decitionaries-----------------")
people = [
    ("Bob", 96, "Mechanic"),
    ("James", 80,"Artist"),
    ("Anne",100, "Lecturer")
]

for name, scores , profession in people:
    print(f"Name: {name}, scores: {scores}, Profession: {profession}")

print("---------------------Print 2 values of 3------------------")

person = ("Bob", 42 , "Mechanic")

name, _ , profession = person
print(name, profession)

print("---------------* symbol in lists--------------------")

suka, *ass = [1,2,3,4,5]
print(suka)
print(ass)
print("-----------------FUNCTIONS----------------")

def add(x,y):
    return x * y

print(add(3,2))
print("-----------------FUNCTIONS2----------------")

def say_hello(name,surname):
    print(f"Hello, {name} {surname}")

say_hello(surname = "Pizda", name = "Huy")

print("--------FUNCTIONS default parameters------------")
default_y=8
def add2(x,y=default_y): #!---default value after declaration is unchangable
    sum = x + y
    return sum

print(add2(5))

print("----------Lambda function----------------")
#! Lanbda function is function which dosent have name, it's only returns values

add3 = lambda x,y: x + y
print(add3(5,7))

print((lambda x,y: x + y)(5,7))

print("----------Lambda function----------------")
def double(x):
    return x *2

sequence = [1,3,5,10]
doubled = [(lambda x: x*2)(x) for x in sequence]

#doubled = list(map(lambda x: x*2, sequence))

print(doubled)
print("----------Dictionary comprehensions----------------")

users = [
    (0,"Bob", "geklas123"),
    (1,"Rolf", "geklas323"),
    (2,"Jose", "12345"),
    (3,"username", "1234")
]

username_mapping = {element[1]:element for element in users} #! - user[1] - сортировка по элементу второму каждого ()

#username_input = input("username: ")
#password_input = input("password: ")

#_,username,password = username_mapping[username_input]

#if  password_input == password:
#    print("it's correct ")
#else:
#    print("Your data is false !")

print("------------------Exercise-----------------")
student = {"name": "Jose", "school": "Computing","grades":(66,77,88)}

def average_grade(data):
    grades = student['grades']
    return sum(grades)/len(grades)

print(average_grade(student))

print("------------------Unpacking arguments-----------------")

#print(multiply(2,3,4))

def apply(*args, operator):
    if operator == "*":
        return multiply(args)
    elif operator =="+":
        return sum(args)
    else:
        return "No valid operator was found"

print(apply(1,3,4,5,operator = "+"))

print("-----------------------")
def add(x,y):
    return x + y

nums = {"x": 15, "y": 25}
print(add(**nums))  #! add(x = nums["x"],y = nums["y"])




print("------------args* operator-----------")
def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg

    return total

def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator =="+":
        return sum(args)
    else:
        return "No valid operator was found"

print(apply(1,3,4,5,operator = "+"))

print("-----------------------")


print("------------Unpacking keywords arguments-----------")

def named(**kwargs):
    print(kwargs)

named(name="Bob", age=25)

print("------------Unpacking keywords arguments-----------")