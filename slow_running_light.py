import time
import threading
import tkinter as tk


class FlashingLightsApp:
    def __init__(self, master):
        self.master = master
        master.title("Slow Running Lights")

        # 步频输入
        self.frequency_label = tk.Label(master, text="Step Frequency (minute):")
        self.frequency_label.pack()

        self.frequency_entry = tk.Entry(master)
        self.frequency_entry.pack()

        # 开始按钮
        self.start_button = tk.Button(master, text="Start", command=self.start_flashing)
        self.start_button.pack()
        # 结束按钮
        self.start_button = tk.Button(master, text="Stop", command=self.stop_flashing)
        self.start_button.pack()

        # 灯的容器
        self.lights_frame = tk.Frame(master, bg="black")
        self.lights_frame.pack(fill=tk.BOTH, expand=True)

        # 创建灯
        self.light = tk.Label(self.lights_frame, bg="black", height=20, width=100)
        self.light.pack_propagate(False)
        self.light.pack(fill=tk.BOTH, expand=True)

        self.flashing = False
        self.frequency = 0
        self.light_thread = 0

    def flash_lights(self):
        print("Flash light thread start...")

        while self.flashing:
            # print("green")
            self.light.config(bg="gray")
            time.sleep(self.frequency)
            # print("blue")
            self.light.config(bg="black")
            time.sleep(self.frequency)

    def start_flashing(self):
        frequency = float(self.frequency_entry.get())
        print("Frequency must be greater than:", frequency)
        if frequency <= 0:
            print("Frequency must be greater than 0")
            return

        if self.flashing:
            print("Light thread has been run")
            return

        self.flashing = True
        self.frequency = round((60 / frequency), 2)
        print(self.frequency)
        self.light_thread = threading.Thread(target=self.flash_lights)
        self.light_thread.start()

    def stop_flashing(self):
        self.flashing = False
        self.light_thread.join()
        print("Flash light thread end...")
        self.light.config(bg="black")


if __name__ == "__main__":
    root = tk.Tk()
    app = FlashingLightsApp(root)
    root.mainloop()
