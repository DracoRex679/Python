import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 125)     # setting up new voice rate
print("""How do you pick up the threads of an old life? How do you go on, when in your heart you begin to understand... there is no going back? There are some things that time cannot mend. Some hurts that go too deep, that have taken hold.""""")
engine.say("""How do you pick up the threads of an old life? How do you go on, when in your heart you begin to understand... there is no going back? There are some things that time cannot mend. Some hurts that go too deep, that have taken hold.""")
engine.runAndWait()
input()