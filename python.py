import tkinter as tk
from time import strftime
import winsound  # Only works on Windows

root = tk.Tk()
root.title("Animated Digital Clock")
root.geometry("500x300")
root.configure(bg="#0F0F0F")

# Labels
time_label = tk.Label(root, font=("Helvetica", 50, "bold"), fg="#00FFCC", bg="#0F0F0F")
time_label.pack(pady=10)

day_label = tk.Label(root, font=("Helvetica", 20), fg="#FFFFFF", bg="#0F0F0F")
day_label.pack()

date_label = tk.Label(root, font=("Helvetica", 20), fg="#AAAAAA", bg="#0F0F0F")
date_label.pack(pady=(0, 20))

# Animation colors
colors = ["#00FFCC", "#00DDCC", "#00BBCC", "#0099CC", "#00BBCC", "#00DDCC"]
color_index = 0

def update_clock():
    global color_index

    # Time elements
    current_time = strftime("%I:%M:%S %p")
    current_day = strftime("%A")
    current_date = strftime("%B %d, %Y")

    # Update labels
    time_label.config(text=current_time, fg=colors[color_index])
    day_label.config(text=current_day)
    date_label.config(text=current_date)

    # Animate color
    color_index = (color_index + 1) % len(colors)

    # Play tick sound
    winsound.Beep(1000, 100)  # Frequency: 1000Hz, Duration: 100ms

    # Repeat
    root.after(1000, update_clock)

update_clock()
root.mainloop()
