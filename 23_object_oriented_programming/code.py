student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}


def average(sequence):
    return sum(sequence) / len(sequence)



class Student:
    def __init__(self_suka, name, grades):   #?=-----__init__   специальное особое название, function inside class called method
        self_suka.name = name  #?----  take all from self and accesing name property inside of self  CREATE ELEMENT CALLED SELF_SUKA
        self_suka.grades = grades

    #?  average - use object which was created upper - init
    def average_grade(self_suka):
        return sum(self_suka.grades) / len(self_suka.grades)

student = Student("Bob",(89, 90, 93, 78, 90))   #? - python create empty container
student2 = Student("Ebllan",(23, 44, 54, 76, 87))  

print(student.average_grade())
print(student.name)
print(student.grades)
print("----------------")
print(student2.average_grade())
print(student2.name)
print(student2.grades)

