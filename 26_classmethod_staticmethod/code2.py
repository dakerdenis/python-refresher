class ClassTest:
    def instance_method(self):   #all functions inside classes which use object as first parameter called instance methods
        print(f"Called instance method of {self}")
        print("suka")

    @classmethod    #метод по умолчанию если в аргументы ничего не добавили то он работает автоматически
    def class_method(cls):    #cls - will be a class itself    cls  ===== ClassTest
        print(f"Called class_method of {cls}")  


#test = ClassTest()  #create object with class test
                    #instance method need an object to call them

#test.instance_method()   #the same as ClassTest.instance_method(test)       
                        #it's called an instance method because u called it on a class instance 

ClassTest.class_method()   #если в аргмент ничего не добавлено питон сам автоматически в аргумент добавит сам класс по себе