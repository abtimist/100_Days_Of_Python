from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global REPS
    window.after_cancel(TIMER)
    timer_text.config(text="Timer")
    canvas.itemconfig(time_text,text="00:00")
    checkmark.config(text="")
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global REPS
    REPS +=1



    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS % 8 == 0:
        timer_text.config(text="Break",fg=RED)
        count_down(long_break_sec)
    elif REPS % 2 == 0:
        timer_text.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_text.config(text="Work", fg=GREEN)
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global TIMER
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time_text, text= f"{count_min}:{count_sec}")
    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start()
        marks = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks += "✅"
        checkmark.config(text=marks)
        checkmark.grid(column=1, row=3)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)


canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
time_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME, 35,"bold"))
canvas.grid(column=1,row=1)

timer_text = Label(text="Timer",font=(FONT_NAME,48,"normal"),fg=GREEN,bg=YELLOW)
timer_text.grid(column=1,row=0)


start_button = Button(text="START",highlightthickness=0,bg="green",fg="white",command=start)
start_button.grid(column=0,row=2)

reset_button = Button(text="RESET",highlightthickness=0,bg=RED,fg="white", command=reset)
reset_button.grid(column=2,row=2)

checkmark = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME,20,"normal"), pady=10)

window.mainloop()