# majdooron ko bulawa
import tasks
import speak
import listen
import screen

# khatarnak Setup
# mere pyaare variables
say = speak.Speech()
browse = tasks.Browser()
do = tasks.System()
hear = listen.Listen()

if __name__ == '__main__':
    say.speak("Welcome User! May I know who you are? If you're a new user say new. ")
    heard = hear.recognize()
    if heard == "new":
        screen.newpg()
        screen.show()
    if "how are you doing today" in heard:
        say.speak("I'm doing great. How about you?")
        heard = hear.recognize()
