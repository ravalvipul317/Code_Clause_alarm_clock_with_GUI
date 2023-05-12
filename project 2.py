from tkinter import *
import time

class AlarmClock:
    def __init__(self, master):
        self.master = master
        master.title("Alarm Clock")

        self.alarm_time_label = Label(master, text="Set Alarm Time:")
        self.alarm_time_label.pack()

        self.alarm_time_entry = Entry(master)
        self.alarm_time_entry.pack()

        self.set_alarm_button = Button(master, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_button.pack()

        self.activate_button = Button(master, text="Activate", command=self.activate_alarm, state=DISABLED)
        self.activate_button.pack()

        self.deactivate_button = Button(master, text="Deactivate", command=self.deactivate_alarm, state=DISABLED)
        self.deactivate_button.pack()

        self.alarm_active = False

    def set_alarm(self):
        alarm_time_str = self.alarm_time_entry.get()
        try:
            alarm_time_struct = time.strptime(alarm_time_str, "%H:%M:%S")
            self.alarm_time = time.mktime(alarm_time_struct)
            self.activate_button.config(state=NORMAL)
        except ValueError:
            pass

    def activate_alarm(self):
        self.alarm_active = True
        self.activate_button.config(state=DISABLED)
        self.deactivate_button.config(state=NORMAL)

        while self.alarm_active:
            current_time = time.time()
            if current_time >= self.alarm_time:
                print("Alarm!")
                break

    def deactivate_alarm(self):
        self.alarm_active = False
        self.deactivate_button.config(state=DISABLED)
        self.activate_button.config(state=NORMAL)

root = Tk()
alarm_clock = AlarmClock(root)
root.mainloop()
