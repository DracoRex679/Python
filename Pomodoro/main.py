from tkinter import *
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def reset_timer():
    global reps
    global timer_text
    window.after_cancel(timer)
    reps = 0
    checks.config(text="")
    header.config(text="Timer")
    canvas.itemconfig(timer_text, text="25:00")



def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    print(reps)

    if reps % 8 == 0:
        header.config(text="Long Break", fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        header.config(text="Short Break", fg=PINK)
        countdown(short_break_sec)
    else:
        header.config(text="Work", fg=GREEN)
        countdown(work_sec)


def countdown(count):
    global timer
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count-1)
    else:
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        checks.config(text=marks)
        start_timer()


window = Tk()
window.title("Tomato")
window.config(padx=100, pady=50, bg=YELLOW)


def say_something(a, b, c):
    print(a)
    print(b)
    print(c)


header = Label()
header.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
header.grid(row=0, column=1)

checks = Label()
checks.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "bold"))
checks.grid(row=3, column=1)

start_button = Button()
start_button.config(text="start", font=("Arial", 12, "normal"), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button()
reset_button.config(text="reset", font=("Arial", 12, "normal"), highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="25:00", fill="green", font=(FONT_NAME, 36, "bold"))
canvas.grid(row=1, column=1)


window.mainloop()
