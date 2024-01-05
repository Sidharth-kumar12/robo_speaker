
import os

import pyttsx3

if __name__ == '__main__':
    print("Welcome to robo speaker")

while True:
    x = input("Enter what you want me to speak: ")
    if x=="q":
        break
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    engine.say(x)
    engine.runAndWait()


