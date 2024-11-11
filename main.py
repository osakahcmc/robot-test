import speech_recognition
import pyttsx3

##______CREATE VARIABLE
robot_ear = speech_recognition.Recognizer()
robot_mount = pyttsx3.init()
robot_brain = ""

while True:

    ##______ROBOT HEAR
    with speech_recognition.Microphone(device_index=2) as mic:
        print("Say something!")
        audio = robot_ear.listen(mic)

    print("Robot:....")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""

    ##______ROBOT UNDERSTAND
    print("You:" + you)
    if you == "":
        robot_brain = "I can't hear you, try again"
    elif "hello" in you:
        robot_brain = "Hello"
    elif "how are you" in you:
        robot_brain = "I'm doing well, thank you"
    elif "bye" in you:
        robot_brain = "Goodbye"
        print("Robot:" + robot_brain)
        robot_mount.say(robot_brain)
        robot_mount.runAndWait()
        break
    else:
        robot_brain = "I don't understand"

    ##______ROBOT SPEAK
    print("Robot:" + robot_brain)
    robot_mount.say(robot_brain)
    robot_mount.runAndWait()