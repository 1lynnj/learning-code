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
reps = 0
timer = None
check_marks = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    global reps
    global check_marks
    check_marks = 0
    reps = 0
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer', fg=GREEN)
    checks.config(text='✓' * check_marks)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global check_marks
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text='Break', fg=RED)
        count_down(long_break_sec)
        checks.config(text='✓' * check_marks)

    elif reps % 2 == 0:
        timer_label.config(text='Break', fg=PINK)
        count_down(5)
        checks.config(text='✓' * check_marks)

    elif reps % 2 != 0:
        timer_label.config(text='Work', fg=GREEN)
        count_down(5)
        check_marks += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)  #window.after(time in milliseconds, function, change in time)
                                                #1000milliseconds equals 1 second
    else:
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro!')
window.config(padx=100, pady=50, bg=YELLOW)

# canvas widget allows things to be layered on top of each other
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  #bg is background color of canvas, highlightthickness is the width of the border of the canvas
tomato_img = PhotoImage(file='tomato.png')
# requires x and y values for position
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

timer_label = Label(text='Timer', font=(FONT_NAME, 55, 'normal'), bg=YELLOW, fg=GREEN, width=5)
timer_label.grid(column=1, row=0)

start = Button(text='Start', highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

checks = Label(text='', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, 'bold'))
checks.grid(column=1, row=3)

reset = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)




# use fg= to set foreground color (ie: text)




# looking for events
window.mainloop()