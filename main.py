#main.py
import tkinter as tk
from tkinter import simpledialog, messagebox
from audio import play_audio

# Global variables to control the timer
is_paused = False
is_stopped = False

def set_timer():
    global is_paused, is_stopped
    # Reset the pause and stop flags
    is_paused = False
    is_stopped = False
    # Hide the start button and show the pause/resume and stop buttons
    set_timer_button.grid_remove()
    pause_resume_button.grid(row=3, column=1, pady=10)
    stop_timer_button.grid(row=3, column=2, pady=10)
    # Þetta fall setur tímann
    try:
        hours = int(hours_entry.get())
        minutes = int(minutes_entry.get())
        seconds = int(seconds_entry.get())

        total_time_sec = hours * 3600 + minutes * 60 + seconds

        countdown(total_time_sec)  # Byrjar að telja niður

    except ValueError:
        messagebox.showerror("Ólöglegt inntak", "Við notum bara tölustafi hér!")

def pause_resume_timer():
    global is_paused
    # Toggle the pause flag
    is_paused = not is_paused
    # Change the button text based on the state of the timer
    if is_paused:
        pause_resume_button.config(text="Halda áfram")
    else:
        pause_resume_button.config(text="Pása")

def stop_timer():
    global is_stopped
    # Set the stop flag
    is_stopped = True
    # Show the start button and hide the pause/resume and stop buttons
    set_timer_button.grid(row=3, column=0, pady=10)
    pause_resume_button.grid_remove()
    stop_timer_button.grid_remove()

def countdown(time_left):
    global is_paused, is_stopped
    if time_left > -1 and not is_stopped:
        # Check if the timer is paused
        if not is_paused:
            # Breytir í sekúntur
            hours = time_left // 3600
            minutes = (time_left % 3600) // 60
            seconds = time_left % 60

            # Breytir labelinu fyrir niðurteljarann
            timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")

            # Byrjar að spila outro lagið þegar 57 sek eru eftir
            if time_left == 57:
                play_audio("output.mp3")

            # Kallar aftur á fallið og minkkar um 1 sek
            root.after(1000, countdown, time_left - 1)
        else:
            # If the timer is paused, call the function again without decreasing the time
            root.after(1000, countdown, time_left)
    else:
        # Tíminn er runninn
        timer_finished()

def timer_finished():
    # Þetta fall keyrist þegar tíminn er runninn
    messagebox.showinfo("Tíminn runninn", "Fókusvinnu er lokið, vel gert!")

# Býr til glugga
root = tk.Tk()
root.title("Fókustími")

# Býr til labels og input fyrir klst, mín, og sek
hours_label = tk.Label(root, text="Klst")
hours_label.grid(row=0, column=0)
hours_entry = tk.Entry(root, width=10)
hours_entry.insert(0, "0")
hours_entry.grid(row=1, column=0, padx=5, pady=5)

minutes_label = tk.Label(root, text="Min")
minutes_label.grid(row=0, column=1)
minutes_entry = tk.Entry(root, width=10)
minutes_entry.insert(0, "0")
minutes_entry.grid(row=1, column=1, padx=5, pady=5)

seconds_label = tk.Label(root, text="Sek")
seconds_label.grid(row=0, column=2)
seconds_entry = tk.Entry(root, width=10)
seconds_entry.insert(0, "0")
seconds_entry.grid(row=1, column=2, padx=5, pady=5)

# Label fyrir niðurteljara
timer_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
timer_label.grid(row=2, column=0, columnspan=3, pady=20)

# Takki sem byrjar tímann
set_timer_button = tk.Button(root, text="Byrja fókus", command=set_timer)
set_timer_button.grid(row=3, column=0, pady=10)

# Takki sem stoppar tímann
stop_timer_button = tk.Button(root, text="Stoppa", command=stop_timer)
stop_timer_button.grid_remove()  # Hide the button initially

# Takki sem pause-ar eða resume-ar tímann
pause_resume_button = tk.Button(root, text="Pása", command=pause_resume_timer)
pause_resume_button.grid_remove()  # Hide the button initially

# Byrjar GUI lykkju
root.mainloop()