from tkinter import *
import time
import datetime
# GUI Window
root = Tk()
root.title("My Alarm")


def setalarm():
    alarmtime = f'{hrs.get()}:{mins.get()}:{secs.get()}'
    print(alarmtime)
    if alarmtime != " : : ":
        alarmclock(alarmtime)


def alarmclock(alarmtime):
    while True:
        time.sleep(1)
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        if time_now == alarmtime:
            text = "Tring..!Tring..!"
            print("Get Up!", text)
            break


hrs = StringVar()
mins = StringVar()
secs = StringVar()

Label(root, text="Hello I'm your new alarm!").grid(row=1, columnspan=3)
hrsbtn = Entry(root, textvariable=hrs, width=5)
hrsbtn.grid(row=2, column=1)
Entry(root, textvariable=mins, width=5).grid(row=2, column=2)
Entry(root, textvariable=secs, width=5).grid(row=2, column=3)
Button(root, text="Set Alarm", command=setalarm).grid(row=4, columnspan=3)
Button(root, text="Set Alarm", command=setalarm).grid(row=4, columnspan=3)
mainloop()
