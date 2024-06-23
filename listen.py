# majdooron ko bulawa
import speech_recognition as sr
import speak

# khatarnak Setup
# mere pyaare variables
recog = sr.Recognizer()
say = speak.Speech()

# Class


class Listen:
    def recognize(self):
        """
        When called turns on mic and returns the audio heard in string form.
        """
        with sr.Microphone() as source:
            print("Listening...")
            audio = recog.listen(source, phrase_time_limit=5)
        try:
            audio = recog.recognize_google(audio).lower()
        except ValueError:
            say.speak("I beg your pardon please!")

        return audio


