# Random-PassWord-Generator

 Python program that generates a random password of a specified length:
 
 Here's how the program works:

    We import the random and string modules. random will be used to generate random characters, and string will be used to define the set of characters to choose from.
    We define a function generate_password() that takes a single argument length indicating the desired length of the password.
    Inside the function, we define a variable characters that contains all the characters we want to include in the password. We use the string.ascii_letters, string.digits, and string.punctuation constants to include upper- and lowercase letters, digits, and punctuation characters, respectively.
    We use the random.choices() function to generate a list of length random characters from the characters set, and then join them together into a single string using the join() method.
    We return the resulting password string from the function.
    We call the generate_password() function with an argument of 8 to generate a password of length 8.
    We print the resulting password string to the console.

You can modify the length of the password by changing the argument to the generate_password() function. You can also modify the set of characters included in the password by modifying the characters variable inside the function.
