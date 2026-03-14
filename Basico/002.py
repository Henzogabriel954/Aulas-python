
import Tools

nameUser = input("What is your name? ")
ageUser = input("What is your age? ")
print(f"\nHello {nameUser}, you are {ageUser} years old. ")
try:
    Tools.pause()
except ValueError:
    print("End...")