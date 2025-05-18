import time
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # Hide the main tkinter window

while True:
    messagebox.showinfo("Alert", "Жаахан амарчих")
    time.sleep(10)  # 30 minutes