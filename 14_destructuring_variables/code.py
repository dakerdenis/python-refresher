t = 5 , 11
x,y = t

print(x,y)


people =[
    ("Bob", 42 , "Bekar"),
    ("James", 24 , "Artist"),
    ("Harry", 32 , "Lecturer")
]

for name, age, profession in people :
    print(f"Name: {name}: {age} profession: {profession}")

head, *tail=[1,2,3,4,5]   #!----в данном случае первое значение 1 - пойдет в head , все остальное в tail
print(head)
print(tail)