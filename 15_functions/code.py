def hello():
    print("Hello suka")


def user__age__in_seconds():
    user_age = int(input("Enter Your age: "))
    age_seconds = user_age * 365 * 24 *60 * 60 * 60
    print(f"Your age in seconds is: {age_seconds}")




print("Suka yebanaya !")


friends = ["Rolf", "Bob"] #!--- one frineds in global 

def add_friend():
    friends.append("eblan") #!---SEcond frineds nside function

add_friend()
print(friends)