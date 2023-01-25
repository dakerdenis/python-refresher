class Test__learning:
    def print_name(self,name):
        print("message1:{}  message2: {}".format(name , name + ' changed'))

    def say_hello(self):
        self.print_name("stalker")


test1 = Test__learning()













class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}   Age: {self.age}")


tom  = Person("Tom",23)
bob = Person("Bob", 38)

#tom.display_info()
#bob.display_info()


class Count:
    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2


    def display_info(self):
        number =  self.number1 + self.number2
        return number

num = Count(1,2)
#print(num.display_info())


class Dog:

    attr1 = "mammal"

    def __init__(self,name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))


Rodger = Dog("Rodger")
Tommy = Dog("Tommy")


Rodger.speak()
Tommy.speak()
