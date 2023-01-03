import time
from tkinter import *
from tkinter import PhotoImage
import winsound
import threading
from tkinter import messagebox

# creating Tk window
root = Tk()

# setting geometry of tk window
root.geometry("400x230+500+50")

root.resizable(0, 0)

# Giving the window some color
root.configure(bg="LightPink1")
# Adding columns
root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=2)
root.columnconfigure(2, weight=2)
root.columnconfigure(3, weight=2)
root.columnconfigure(4, weight=2)

# Using title() to display a message in
# the dialogue box of the message in the
# title bar.
root.title("Time Counter")

# Declaration of variables
hour = StringVar()
minute = StringVar()
second = StringVar()
message = StringVar()

# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")

# Use of Entry class to take input from the user
hourEntry_label = Label(root, text="Hour")
hourEntry_label.grid(column=1, row=0, sticky=E)
hourEntry = Entry(root, width=2, font=("Arial", 18, ""),
                  textvariable=hour)
hourEntry.grid(column=1, row=1, sticky=E)

minuteEntry_label = Label(root, text="Minutes")
minuteEntry_label.grid(column=2, row=0, pady=10)
minuteEntry = Entry(root, width=2, font=("Arial", 18, ""),
                    textvariable=minute)
minuteEntry.grid(column=2, row=1)

secondEntry_label = Label(root, text="Seconds")
secondEntry_label.grid(column=3, row=0, sticky=W)
secondEntry = Entry(root, width=2, font=("Arial", 18, ""),
                    textvariable=second)
secondEntry.grid(column=3, row=1, sticky=W)

# field to enter message you want to show up in pop up window when time is up
messageEntry = Entry(root, width=14, font=("Arial", 18, ""),
                     textvariable=message)
messageEntry.grid(column=2, row=6, pady=10, padx=5)


# Pop-up window when time is up
def open_topLevel():
    # Using winsound to play a sound when TopLevel window appears
    winsound.PlaySound("alarm.wav", winsound.SND_ASYNC)
    top = Toplevel()
    # Changing background color just for fun.
    top.configure(bg="LightPink1")
    # Using zoomed to make the pop-up window maximized
    top.state("zoomed")
    top.title("Finished")
    top.bgPic = PhotoImage(file="deadpoolBG.gif")  # Assign the image to an attribute of the Toplevel widget
    top_background = Label(top, image=top.bgPic)
    top_background.pack()
    top_label = Label(top, text="Time's up!", font=("Helvetica", 20, "bold"), bg="LightPink1",
                      fg="#8B0000")
    # Another label to display the message from the input window
    top_label_message = Label(top, text=message.get(), font=("Helvetica", 20, "bold", "underline"), bg="LightPink1",
                              fg="#8B0000")
    # Button to go back to main window.
    top_btn = Button(top, text="Thank you!", borderwidth=3, relief="raised", font=("Helvetica", 15),
                     command=top.destroy)
    top_label.pack(pady=5)
    top_label_message.pack(pady=5)
    top_btn.pack(pady=10)

#Variable set to false to be able to stop thread later
stop_thread = False

#Function to reset timer down to zero and stop the timer
def reset_timer():
    global stop_thread
    stop_thread = True
    hour.set("00")
    minute.set("00")
    second.set("00")

#Function for the timer itself with input from user
def submit():
    global stop_thread
    stop_thread = False
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        print("Please input the right value")
    while not stop_thread and temp != -1:

        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins, secs = divmod(temp, 60)

        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours = 0
        if mins > 59:
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)

        # using format () method to store the value up to
        # two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        time.sleep(1)
        # when temp value = 0; then a messagebox pop's up
        # and message from user input
        if temp == 0:
            # messagebox.showinfo("Time Countdown", "Time's up \n" + message.get())
            open_topLevel()

        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1


# button widget
start_btn = Button(root, text='Set Time Countdown', bd='5',
                   command=submit)
start_btn.grid(column=2, row=8, padx=5, pady=5)
#Button to stop the countdown and reset the timer
reset_button = Button(root, text="Reset Timer", bd='5', command=reset_timer)
reset_button.grid(column=2, row=9, padx=5, pady=5)

# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
root.mainloop()
