import time, wget, os
from playsound import playsound
print("Hey there, Thanks for using the countdown timer!!")
hour = int(input("How many hours would you like to create your countdown timer for? (If it is less than a hour enter 0)"))
hours = hour * 3600
minute = int(input("How many minutes would you like to create your countdown timer for? (If it is less than a minute enter 0)"))
minutes = minute * 60
seconds = int(input("How many seconds would you like to create your countdown timer for?"))
full_seconds = hours + minutes + seconds
while (full_seconds == 0) == False:
    print(str(full_seconds) + " seconds left")
    time.sleep(1)
    full_seconds = full_seconds - 1
else:
    wget.download("https://github.com/Samthebest999/Python-Count-Down-Timer/raw/main/AlarmClock.wav")
    try:
        playsound("AlarmClock.wav")
    except KeyboardInterrupt:
        time.sleep(2)
        if os.path.exists("AlarmClock.wav"):
            os.remove("AlarmClock.wav")
    if os.path.exists("AlarmClock.wav"):
        os.remove("AlarmClock.wav")