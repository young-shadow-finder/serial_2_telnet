import time
import psutil
import threading
import tkinter as tk
from tkinter import messagebox


# battery
local_battery = psutil.sensors_battery()
# delay time
next_check_period = 30000


def check_battery():
    global local_battery
    global next_check_period

    if local_battery is None:
        label.config(text=f"No Battery...")
        next_check_period = 300000  # 5min check
    else:
        current_battery_percent = local_battery.percent
        label.config(text=f"Battery Power : {current_battery_percent}%")
        if current_battery_percent <= 20:
            messagebox.showinfo("Notify", f"Battery just left {current_battery_percent}%！Please charge...")
            next_check_period = 30000  # 30s check
        elif current_battery_percent >= 85 and local_battery.power_plugged:
            messagebox.showinfo("Notify", f"Battery now {current_battery_percent}%，charging could stop")
            next_check_period = 30000  # 30s check

    root.after(next_check_period, check_battery)
    next_check_period = 120000  # default 2sec check


if __name__ == '__main__':
    # main root
    root = tk.Tk()
    root.geometry("350x80")
    root.title("Youngの電池充電助手")

    label = tk.Label(root, text="checking battery...", font=("Arial", 16))
    label.pack(pady=20)

    check_battery()

    root.mainloop()
