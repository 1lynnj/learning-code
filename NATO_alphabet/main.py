# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

with open('nato_phonetic_alphabet.csv') as data:
    alpha_data = data.readlines()

nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')
# print(nato_data)

# new_dict = {new_key:new_value for (index, row) in DataFrame.itterrows()
# itterows accesses the values in each row
nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}
# print(nato_dict)




# new_list = [new_item for item in list]

## my code for catching an error
error = True
while error:
    try:
        user_name = input("What is your name? ").upper()
        code_list = [nato_dict[letter] for letter in user_name]
        print(code_list)
        error = False

    except KeyError:
        print('Sorry, only letters in the alphabet please.')

####Angela's code for above

# def generate_phonetic():
#     user_name = input("Enter a word. ").upper()
#     try:
#         code_list = [nato_dict[letter] for letter in user_name]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         generate_phonetic()
#     else:
#         print(code_list)
#
# generate_phonetic()
