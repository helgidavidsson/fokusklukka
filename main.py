#main.py
import tkinter as tk
from tkinter import simpledialog, messagebox
from audio import play_audio


def set_timer():
    # Þetta fall setur tímann
    try:
        hours = int(hours_entry.get())
        minutes = int(minutes_entry.get())
        seconds = int(seconds_entry.get())

        total_time_sec = hours * 3600 + minutes * 60 + seconds

        countdown(total_time_sec)  # Byrjar að telja niður

    except ValueError:
        messagebox.showerror("Ólöglegt inntak", "Við notum bara tölustafi hér!")


def countdown(time_left):
    if time_left > -1:
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
        # Tíminn er runninn
        timer_finished()


def timer_finished():
    # Þetta fall keyrist þegar tíminn er runninn
    messagebox.showinfo("Tíminn runninn", "Fókusvinnu er lokið, vel gert!")


# Býr til glugga
root = tk.Tk()
root.title("Fókustími")

# Býr til input fyrir klst, mín, og sek
hours_entry = tk.Entry(root)
hours_entry.insert(0, "Klst")
hours_entry.pack(pady=5)

minutes_entry = tk.Entry(root)
minutes_entry.insert(0, "Min")
minutes_entry.pack(pady=5)

seconds_entry = tk.Entry(root)
seconds_entry.insert(0, "Sek")
seconds_entry.pack(pady=5)

# Label fyrir niðurteljara
timer_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
timer_label.pack(pady=20)


# Takki sem byrjar tímann
set_timer_button = tk.Button(root, text="Byrja fókus", command=set_timer)
set_timer_button.pack(pady=10)

# Byrjar GUI lykkju
root.mainloop()
