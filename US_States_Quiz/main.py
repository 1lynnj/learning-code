from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.setup(width=800, height=600)
screen.bgpic('blank_states_img.gif')
screen.title('US State Game')

data = pandas.read_csv('50_states.csv')
data_dict = data.to_dict()
# print(data_dict)

# list to run game loop only if guess in list
states = []
for key in data_dict['state']:
    states.append(data_dict['state'][key])

score = 0
guessed_states = []

game_on = True
while game_on:
    player_guess = screen.textinput(f'{score}/50', 'Name a state: ').title()
    # print(f'guess: {player_guess}')
    if player_guess == "Exit":
        # create a csv file of states not guessed
        missing_states = [state for state in states if state not in guessed_states]

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')

    if player_guess in states:
        score += 1
        guessed_states.append(player_guess)
        for key in data_dict['state']:
            # print(data_dict['state'][key])
            x = data_dict['x'][key]
            y = data_dict['y'][key]
            if player_guess == data_dict['state'][key]:
                # player = True
                state = Turtle()
                state.hideturtle()
                state.penup()
                # print(f'Guess: {player_guess}')
                state.goto(x, y)
                state.write(f'{player_guess}', font=('Arial', 8, 'normal'))

    else:
        lost = Turtle()
        lost.hideturtle()
        lost.penup()
        lost.goto(-150, 0)
        lost.write(f'{player_guess} is wrong!', font=('Arial', 40, 'normal'))
        game_on = False



# screen.exitonclick()



# keeps screen open even though the code is done running. alternaitve to exit on click
# turtle.mainloop()


## this gets the x and y coordinates for anywhere you click on the screen. Angela did this and compiled the
# data in a csv file. Not needed to run the game.
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
