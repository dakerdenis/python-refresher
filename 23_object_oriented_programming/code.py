student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

                                        #student - it's not a student it's dictionary with data called student


                                                    #self - стандартный аргумент который обозначает то что мы суем в этот класс
                                                        #all methods in class should has a parameter
class Student:                                          # - it dsnt create a student it only says how it'll be behave
    def __init__(self,name, grades):                                 #it takes whatever self is , and acces name property of self,
        self.name = name                              # and give value for name / create property  #name - property inside given data
        self.grades = grades
    
    def average(self):                                  #method takes self as parameter , all methods inside the class should take a parameter, wich will be an object 
        return sum(self.grades) / len(self.grades)      #which was created initially
        

student = Student("Bob",(89, 90, 93, 78, 90))                                     #python create object/empty container called student
                                                        #python give back self

student2 = Student("Ralf",(11, 100, 54, 78, 90)) 
 
#print(student.name)
#print(student.grades)
print(student.average())                                 #call object called student which containt method inside of it

print(student2.average())     

