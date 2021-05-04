import time, wget
from playsound import playsound
print("Hey there, Thanks for using the countdown timer!!")
wyltkwabw = input("So, now would you like to know why you should use this count down timer instead of one you found on the web Yes/No (Case Sensitive)")
if wyltkwabw == "Yes":
    print("""
    The reasons you should use this countdown clock and not some clock you find on the internet are:
    1. It is very lightweight, and it is great beacuse your browser takes a heavy load on your computer... you can leave this open in the background and it will use very little computer resources as it is coded in python.
    2. It is very fast unlike the ones on the web browser the javascript for those websites is very complicated and has a slower execution time. My program runs on simple subtraction and displaying numbers so it is much faster.
""")
elif wyltkwabw == "No":
    print("Ok We will continue")
hour = int(input("How many hours would you like to create your countdown timer for? (If it is less than a hour enter 0)"))
hours = hour * 3600
minute = int(input("How many minutes would you like to create your countdown timer for? (If it is less than a minute enter 0)"))
minutes = minute * 60
seconds = int(input("How many seconds would you like to create your countdown timer for?"))
full_seconds = hours + minutes + seconds
while full_seconds > 0:
    print(full_seconds - 1 + " seconds left")
    time.sleep(1)
else:
    playsound("https://github.com/Samthebest999/Python-Count-Down-Timer/raw/main/Alarm%20Clock.wav")