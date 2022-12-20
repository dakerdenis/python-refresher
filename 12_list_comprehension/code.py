a= 1
#!-----List comprehesion - позволяет сразу налету создавать список из уже имеющегося списка
#! -- пример внизу находит список из чисел 
numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers ] #!-- сразу добавляет в список по одному значения из списка выше сразу умнажая их на 2
print(doubled)









friends = ["Sam", "Stalker", "Samantha"]

start_s = [name for name in friends if name.startswith("S")]
#!-- friends и новый список start_s который создан с нуля, они могут иметь одинаковые значения,но они разные сами по себе поскольку занимают разные места в памяти
#for friend in friends:
#    if friend.startswith("S"):
#        start_s.append(friend)

print(start_s)