import time
import tkinter
from tkinter import *
root = Tk()
root.title("Pomodoro Timer")
root.geometry("250x150")
root.configure(background='red')

global is_on
is_on = FALSE

sec = StringVar()
mins = StringVar()
sec.set('00')
mins.set('00')

def reset():
    sec.set('00')
    mins.set('00')
    StudyBreakLabel.config(text="Ready?")

def on():
    while is_on:
        countdown()

def countdown():
    t = 1500
    while t > -1:
        if is_on == FALSE:
            reset()
            break
        StudyBreakLabel.config(text="Study")
        m, s = divmod(t, 60)
        sec.set("{:02d}".format(s))
        mins.set("{:02d}".format(m))
        root.update()
        time.sleep(1)
        t -= 1
    t = 300
    while t > -1:
        if is_on == FALSE:
            reset()
            break
        StudyBreakLabel.config(text="Break")
        m, s = divmod(t, 60)
        sec.set("{:02d}".format(s))
        mins.set("{:02d}".format(m))
        root.update()
        time.sleep(1)
        t -= 1

def switch():
    global is_on
    if is_on:
        StartStopButton.config(text="Start")
        is_on = FALSE
    else:
        StartStopButton.config(text="Reset")
        is_on = TRUE
        on()

def initialstart():
    global is_on
    is_on = TRUE
    StartButton.destroy()
    on()

StudyBreakLabel = Label(root, text="Ready?", bg='red', fg = 'white')
StudyBreakLabel.pack(pady=20)

minsLabel = Label(root, textvariable=mins, bg='red', fg = 'white')
minsLabel.place(x=102,y=55)

TimerLabel = Label(root, text=':', bg='red', fg = 'white')
TimerLabel.place(x=120,y=55)

secLabel = Label(root, textvariable=sec, bg='red', fg = 'white')
secLabel.place(x=128,y=55)

StartStopButton = Button(root, text="Reset", bg='white', fg = 'red', width = 10, command=switch)
StartStopButton.place(x=85,y=100)

StartButton = Button(root, text="Start", bg='white', fg = 'red', width = 10, command=initialstart)
StartButton.place(x=85,y=100)

root.mainloop()