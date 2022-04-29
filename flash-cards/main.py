from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

card = {}
word_list = {}

# ----------------------------------GET DATA----------------------------- #
try:
    data = pandas.read_csv('data/words_to_learn.csv')   # creates a Data Frame
    print(data)
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    word_list = original_data.to_dict(orient='records')   # creates a list of dictionaries. without the orient parameter, it creates a nested dict of french words with key "french" and english words with key "english"
else:
    word_list = data.to_dict(orient='records')  # this is a to_dict parameter that will create a list of dictionaries of key, value pairs by data frame column
    print(word_list)

# card = random.choice(word_list)


# ----------------------------------NEW CARD----------------------------- #

def new_card():
    global card, timer
    window.after_cancel(
        timer)  # cancels timer before each new card so that timer restarts (code at end of function to restart) if you click through new cards quickly
    card = random.choice(word_list)
    canvas.itemconfig(image, image=card_front_image)
    canvas.itemconfig(language_title, text='French', fill='black')
    canvas.itemconfig(word, text=card['French'], fill='black')
    timer = window.after(3000, flip_card)


# ----------------------------------FLIP CARD----------------------------- #


def flip_card():
    canvas.itemconfig(image, image=card_back_image)
    canvas.itemconfig(language_title, text='English', fill='white')
    canvas.itemconfig(word, text=card['English'], fill='white')


# ----------------------------------SAVE DATA----------------------------- #

def is_known():
    word_list.remove(card)
    print(len(word_list))
    data = pandas.DataFrame(word_list)
    data.to_csv('data/words_to_learn.csv',index=False)
    new_card()


# ----------------------------------UI SETUP----------------------------- #


window = Tk()
window.title('Flash Cards')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file='images/card_front.png')
card_back_image = PhotoImage(file='images/card_back.png')
image = canvas.create_image(400, 263, image=card_front_image)
language_title = canvas.create_text(400, 150, text='', font=("Arial", 40, 'italic'))
word = canvas.create_text(400, 263, text='', font=("Arial", 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file='images/right.png')
right_button = Button(window, image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=0, row=1)

idk_image = PhotoImage(file='images/wrong.png')
idk_button = Button(image=idk_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=new_card)
idk_button.grid(column=1, row=1)

timer = window.after(3000, flip_card)
new_card()

window.mainloop()
