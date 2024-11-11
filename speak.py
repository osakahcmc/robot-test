import pyttsx3

robot_brain = "Hello"

robot_mount = pyttsx3.init()
robot_mount.say(robot_brain)
robot_mount.runAndWait()