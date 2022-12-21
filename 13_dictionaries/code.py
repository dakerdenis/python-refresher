friends_ages = {"Rolf": 34, "Denis": 25 , "Stalker": 45}

friends_ages["Rolf"] = 20
friends_ages["Bob"] = 19

print(list(friends_ages.items())) #!-we recieve back list of touples

for t in friends_ages.items():   #!--- печатает touple each separately
    print(t)
for student, age in friends_ages.items():   #!--- печатает touple each separately
    print(f"{student}: {age}")

friends_age = friends_ages.values() #!--values - берёт вместо ключей только значения
friends__avg_age = sum(friends_age)/len(friends_age)
#print(friends__avg_age)


#for student, attendance in friends_ages.items():
   # print(f"{student}: {friends_ages[student]}")
  #  print(f"{student}: {attendance}")
# print(friends_ages["Rolf"])

friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Denis", "age": 25},
    {"name": "Stalker", "age": 45}

]
#print(friends[0]["name"])