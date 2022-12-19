name = "Bob" 

#print(f"Hello, {name}") #! f - позволяет менять строку внутри и вставлять значения какие угодно в момент времени получения

name = "Rolf"

#print(f"Hello, {name}")


#!------Strings with fomat method

name = "Pidaraz"
greeting = "Hello, {}"
with_name = greeting.format(name) #! format - заменяет скобки на значения которые в него заложены
with_name_two = greeting.format("ebanat");

#print(with_name)
#print(with_name_two)

#!------Loger tempplates

longer__phrase = "Hello , {}. Today is {}."

formatted = longer__phrase.format("Eblan", "Monday")

print(formatted)