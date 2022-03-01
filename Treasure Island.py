import pyttsx3
engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

print("Welcome to Treasure Island \n Your mission is to find the treassure")
tPoint = "<----------|---------->"
tPoint2 ="           ^           "
tPoint3 ="           |           "
c1 = "         __________ "
c2 = "        /\____;;___\ "
c3 = "       | /         / "
c4 = "       `. ())oo() . "
c5 = "        |\(%()*^^()^\ "
c6 = "       %| |-%-------| "
c7 = "      % \ | %  ))   | "
c8 = "      %  \|%________| "
print(tPoint + "\n" + tPoint2 + "\n" + tPoint3)
speak("Here's a T-point where would you like to go?:")
rightLeft = input("Here's a T-point where would you like to go?: ")

if rightLeft.lower() == "left":
    speak("I think that you are on the right path! ")
    print("I think that you are on the right path! (^_^)")
    speak("OH! NO! THERE IS A RIVER, WOULD YOU LIKE TO WAIT OR SWIM?:")
    swimWait = input("OH! NO! THERE IS A RIVER, WOULD YOU LIKE TO WAIT OR SWIM?:")

    if swimWait.lower() == "wait":
        speak("I think that you are on the right path!")
        print("I think that you are on the right path!")
        speak("OH! YES! THERE ARE THREE WHICH HAVE EMERGED FROM THE RIVER ONE BLUE RED YELLOW, FROM WHICH GATE SHOULD I GET IN?: ")
        whichDoor = input("OH! YES! THERE ARE THREE WHICH HAVE EMERGED FROM THE RIVER ONE BLUE RED YELLOW, FROM WHICH GATE SHOULD I GET IN?: ")
    
        if whichDoor.lower() == "yellow":
            speak('YOU WON YOU ARE THE BEST PIRATE')
            print("YOU WON YOU ARE THE BEST PIRATE")
            print(c1 + "\n" + c2 + "\n" + c3 + "\n" + c4 + "\n" + c5 + "\n" + c6 + "\n" + c8)
        else:
            print("OH! you just won the game \n you were burned by lava \n /\ \n / \ \n /  \ \n /   \ ")
    else:
        print("OH! you were attacked by trout!!!!")
else:
    print("Opps... You fall into a giant hole")

