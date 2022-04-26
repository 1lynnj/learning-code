from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=350, height=150)
window.config(padx=50, pady=40)

input_miles = Entry(width=7)
input_miles.grid(column=1, row=0)

miles_label = Label(text='Miles', font=('Arial', 20, 'normal'))
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text='is equal to', font=('Arial', 20, 'normal'))
is_equal_to_label.grid(column=0, row=1)

converted_km_label = Label(text=' ', font=('Arial', 20, 'normal'))
converted_km_label.grid(column=1, row=1)

km_label = Label(text='Km', font=('Arial', 20, 'normal'))
km_label.grid(column=2, row=1)


def calculate_button():
    conversion = f'{round(float(input_miles.get()) * 1.609344)}'
    converted_km_label.config(text=conversion)


calculate = Button(text='Calculate', font=('Arial', 18, 'normal'), command=calculate_button)
calculate.grid(column=1, row=2)

window.mainloop()
