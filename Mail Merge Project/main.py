# Open starting_letter file and get message template
with open('./Mail Merge Project Start/Input/Letters/starting_letter.txt',
          mode='r') as body:
    message = body.read()
    # print(message)

# open and loop through names in invited_names file, for each name replace placeholder in message file with name and save new letter in file
with open('./Mail Merge Project Start/Input/Names/invited_names.txt',
          mode='r') as invited_names:
    for name in invited_names:
        greeting = f'{name.strip()}'
        # print(greeting)
        new_letter = message.replace('[name]', greeting)
        # print(new_letter)
        # open the file to write to
        with open(f'./Mail Merge Project Start/Output/ReadyToSend/{greeting}_letter.txt', mode='w') as new_file:
            new_file.write(new_letter)
