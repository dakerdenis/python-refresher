number = 7


while True:   #!--- создаёт безконечный loop
    user_input = input("Enter 'y' if you would like to play: ")

    if user_input =="n":
        break

    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
        break
    elif abs(number - user_number) == 1:   
        print("You were off by 1.")
    else:
        print("Sorry, it's wrong!") 

frineds = ["Eblan1" , "Eblan2", "Eblan3", "Eblan4"]

#for friend in frineds:
    #print(f"{friend} is Eblan suka")

grades = [35, 67,98,23,13]
total = sum(grades)   #!-----sum() суммирует все значения в массиве или списке
amount = len(grades)  #!-----len() выдаёт значение в виде длины массива или списка

print(total/amount)
