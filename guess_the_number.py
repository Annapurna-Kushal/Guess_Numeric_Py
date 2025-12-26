import tkinter as tk

low = 1
high = 100
count = 0

def guess():
    global mid, count
    mid = (low + high) // 2
    count += 1
    label.config(text=f"Is your number {mid}?")
    counter.config(text=f"Guesses: {count}")

def higher():
    global low
    low = mid + 1
    guess()

def lower():
    global high
    high = mid - 1
    guess()

def correct():
    label.config(text=f"🎉 I guessed it in {count} tries!")
    disable_buttons()

def restart():
    global low, high, count
    low = 1
    high = 100
    count = 0
    enable_buttons()
    label.config(text="Think of a number between 1 and 100")
    counter.config(text="Guesses: 0")
    guess()

def disable_buttons():
    btn_higher.config(state="disabled")
    btn_lower.config(state="disabled")
    btn_correct.config(state="disabled")

def enable_buttons():
    btn_higher.config(state="normal")
    btn_lower.config(state="normal")
    btn_correct.config(state="normal")

root = tk.Tk()
root.title("AI Guessing Game")
root.geometry("400x260")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

label = tk.Label(
    root,
    text="Think of a number between 1 and 100",
    font=("Segoe UI", 13),
    fg="white",
    bg="#1e1e1e"
)
label.pack(pady=20)

counter = tk.Label(
    root,
    text="Guesses: 0",
    font=("Segoe UI", 10),
    fg="#e47979",
    bg="#535151"
)
counter.pack()

frame = tk.Frame(root, bg="#e88383")
frame.pack(pady=20)

btn_lower = tk.Button(frame, text="Lower", width=10, command=lower)
btn_lower.grid(row=0, column=0, padx=5)

btn_correct = tk.Button(frame, text="Correct", width=10, command=correct)
btn_correct.grid(row=0, column=1, padx=5)

btn_higher = tk.Button(frame, text="Higher", width=10, command=higher)
btn_higher.grid(row=0, column=2, padx=5)

btn_restart = tk.Button(root, text="Restart", width=12, command=restart)
btn_restart.pack(pady=10)

guess()
root.mainloop()
