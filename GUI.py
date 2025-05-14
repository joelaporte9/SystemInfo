import tkinter as tk
from tkinter import ttk
from CpuUtility import cpu
import psutil

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Computer Usage Monitor")
        self.root.geometry("300x150")
        self.cpu = cpu()

        # CPU Usage Label
        self.label = ttk.Label(self.root, text="CPU Usage: ", font=("Helvetica", 14))
        self.label.pack(pady=20)
        self.label = ttk.Label(self.root, text="CPU Freq: ", font=("Helvetica", 14))
        self.label.pack(pady=20)

        # Update CPU usage every second
        self.update_cpu_usage()
        self.update_cpu_freq()

    def update_cpu_usage(self):
        usage_percent = self.cpu.get_usage_percent()
        self.label.config(text=f"CPU Usage: {usage_percent}%")
        
        self.root.after(1000, self.update_cpu_usage)

    def update_cpu_freq(self):
        cpu_freq = self.cpu.get_cpu_frequency()
        self.label.config(text=f"CPU Frequecy: {cpu_freq}")
        
        self.root.after(1000, self.update_cpu_freq)

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
