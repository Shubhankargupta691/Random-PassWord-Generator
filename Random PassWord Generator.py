import random
import string

while True:
    print(" Press 1. To    Press 0. to Exit")
    user = int(input("Enter your choice: "))
    if user == 1:
        passwordlen = int(input("enter the length of your password"))

        # s = ("asdfghjklqwertyuiopzxcvbnm!@#$%^&*()_-=+/*1234567890("")<{}['']?\|;:ASDFGHJKLZXCVBNMQWERTYUIOP<>")
        # Define the character set to use in the password
        s = string.ascii_letters + string.digits + string.punctuation

        # password
        p = "".join(random.sample(s, passwordlen))
        print("Your RANDOMLY GENERATED PASSWORD is: ", p)
    elif user == 0:
        print("YOU ARE EXIT")
        break

    else:
        print("Invalid Choice")
        break
