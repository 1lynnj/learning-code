from art import logo
from art import vs
from game_data import data
import random

    # guess becomes choice_a, random sample from data again = choice_b
    # repeat code until computer > player

print(logo)

compare_a = random.sample(data, 1)
print(f"a is {compare_a}")
compare_b = random.sample(data, 1)
print(f"b is  {compare_b}")
compare_c = random.sample(data, 1)
print(f"c is {compare_c}")

player_answer = 0
unchosen_answer = 0
current_score = 0

while player_answer >= unchosen_answer:

    print(f"Compare A: {compare_a[0]['name']}, a {compare_a[0]['description']}, from {compare_a[0]['country']}")

    print(vs)

    print(f"Compare B: {compare_b[0]['name']}, a {compare_b[0]['description']}, from {compare_b[0]['country']}")

    guess = input("Who has more followers? Type 'A' or 'B'. ").lower()

    if guess == "a":
        player_answer = compare_a[0]['follower_count']
        print(f"Player: {player_answer}") # check
        unchosen_answer = compare_b[0]['follower_count']
        print(f"Unchosen answer: {unchosen_answer}") # check

    if guess == "b":
        player_answer = compare_b[0]['follower_count']
        print(f"Player answer: {player_answer}") # check
        unchosen_answer = compare_a[0]['follower_count']
        print(f"Unchosen answer: {unchosen_answer}") # check
    
    if player_answer > unchosen_answer:
        current_score += 1
        print(f"Your score is: {current_score}.")
        if guess == "b":
            compare_a = compare_b
        elif guess == "a":
            compare_a = compare_a

        compare_b = compare_c    

    else:
        print(f"Sorry, that's wrong. Final score: {current_score}.")
