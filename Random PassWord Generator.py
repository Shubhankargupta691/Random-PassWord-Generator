import random

while 1:
    print(" Press 1. To    Press 0. to Exit")
    user = int(input("Enter your choice: "))
    if user == 1:
        passwordlen = int(input("enter the length of your password"))
        s = ("asdfghjklqwertyuiopzxcvbnm!@#$%^&*()_-=+/*1234567890("")<{}['']?\|;:ASDFGHJKLZXCVBNMQWERTYUIOP<>")
        p = "".join(random.sample(s,passwordlen))
        print("Your RANDOMLY GENERATED PASSWORD is:",p)
    elif user == 0:
        print("YOU ARE EXIT")
        break
        
    else:
        print("Invalid Choice")
        break