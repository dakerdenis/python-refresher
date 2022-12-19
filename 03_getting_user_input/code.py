name = input("Can you write your name: ")
user_name = "Hi eblan {}"
user__result = user_name.format(name)

size__input = input("How big is your penis: ") #!----Выдаёт всё только в виде String
square__feet = int(size__input)

square__meters = square__feet/2


square__user__result = "Your penis was {}  now is 2 times smaller: {} sm "
square__user__final = square__user__result.format(square__feet,square__meters)


print(user__result + "," +  square__user__final)