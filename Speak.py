import pyttsx3
#pip install pyttsx3


def Say(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[1].id)
    engine.setProperty('rate', 170)
    print("   ")
    print(f"Ana : {Text}" )
    engine.say(text=Text)
    engine.runAndWait()
    print("    ")  
#Say("Hello, I am Ana")

