import speech_recognition

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone(device_index=2) as mic:
    print("Say something!")
    audio = robot_ear.listen(mic)

try:
    you = robot_ear.recognize_google(audio)
except:
    you = ""

print("You:" + you)