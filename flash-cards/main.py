from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'Arial'


# ----------------------------------GET DATA----------------------------- #

data = pandas.read_csv('data/french_words.csv')
word_list = data.to_dict(
    orient='records')  # this is a to_dict parameter that will create a list of dictionaries of key, value pairs by column
# print(word_list)
card = random.choice(word_list)

# ----------------------------------NEW CARD----------------------------- #

def new_card():
    card = random.choice(word_list)
    canvas.itemconfig(language_title, text='French')
    canvas.itemconfig(word, text=card['French'])

# ----------------------------------FLIP CARD----------------------------- #


def flip_card():
    canvas.itemconfig(image, image=card_back_image)
    canvas.itemconfig(language_title, text='English')
    canvas.itemconfig(word, text=card['English'])

# ----------------------------------UI SETUP----------------------------- #


window = Tk()
window.title('Flash Cards')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file='images/card_front.png')
card_back_image = PhotoImage(file='images/card_back.png')
image = canvas.create_image(400, 263, image=card_front_image)
language_title = canvas.create_text(400, 150, text='French', font=(FONT_NAME, 40, 'italic'))
word = canvas.create_text(400, 263, text=card['French'], font=(FONT_NAME, 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file='images/right.png')
right_button = Button(window, image=right_image, highlightthickness=0, command=flip_card)
# right_button.bind('<Return>', new_card())
right_button.grid(column=0, row=1)

idk_image = PhotoImage(file='images/wrong.png')
idk_button = Button(image=idk_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=flip_card)
idk_button.grid(column=1, row=1)




window.mainloop()
