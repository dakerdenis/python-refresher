def named(**kwargs):
    print(kwargs)
#?named(name="Bob", age = 25)
#?{'name': 'bob', 'age': 25}



def named2(name, age):
    print(name, age)

details  = {"name": "Bob", "age":25}

# ? named2(details) - ошибка при выполнений потому что детали это словарь,а мы вставляем его как аргумент какой то там. named2(1аргумент, 2аргумент)

#?named2(details,25)
#?{'name': 'Bob', 'age': 25} 25
#?   named2(**details)  #? ----- автоматом назначает аргументы,сокращает запись ,распаковывает словарь на составляющие
# *------------------------------------------------------------------------#
print("---------------------656646------------------------")
def print_nicely(**kwargs):
    named(**kwargs)
    for suka, suka_value in kwargs.items():
        print(f"{suka}: {suka_value}")

print_nicely(name="Bob", age=25)

print("------------------------------------------------------")

def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1,3,4, name = "bob", age  = 25)
