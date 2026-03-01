def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()


# On peut stocker la fonction dans une variable.
# On peut passer la fonction en tant que paramètre à une autre fonction.
def greet(func):
    # storing the function in a variable
    greeting = func("Hi, I am created by a function passed as an argument.")
    print(greeting)

greet(shout)
greet(whisper)