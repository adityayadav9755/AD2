# majdooron ko bulawa
import pyttsx3

# khatarnak Setup
# mere pyaare variables
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 170)
engine.setProperty('volume', 0.8)
engine.setProperty('voice', voices[0].id)

# Class


class Speech:

    def speak(self, speech):
        """
        Takes string as argument and makes computer speak that in audio form.
        """
        engine.say(speech)
        engine.runAndWait()
