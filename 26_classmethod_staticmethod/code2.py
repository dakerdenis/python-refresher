class ClassTest:
    def instance_method(self):   #all functions inside classes which use object as first parameter called instance methods
        print(f"Called instance method of {self}")
        print("suka")

    #instance method used - when u want action data inside object  which for exmp was created before
    #or call method for modifi method

    @classmethod    #метод по умолчанию если в аргументы ничего не добавили то он работает автоматически
    def class_method(cls):    #cls - will be a class itself    cls  ===== ClassTest
        print(f"Called class_method of {cls}")  
    
    #if u need function which  use class or anyting - classmethod
    #функция если что то  с классом надо делать с данными
    #used more in factories


    @staticmethod
    def static_method():   #this method don't get anything  
        print("Called static method")
    #if u need function which dosn't use class or anyting - static
    #Функция если с классом ничего делать не нужно и она просто должна выполнится не влияя на сам класс
    #class - идет как контейнер в котором рандомные функции расположены



#test = ClassTest()  #create object with class test
                    #instance method need an object to call them

#test.instance_method()   #the same as ClassTest.instance_method(test)       
                        #it's called an instance method because u called it on a class instance 

ClassTest.static_method()   #если в аргмент ничего не добавлено питон сам автоматически в аргумент добавит сам класс по себе