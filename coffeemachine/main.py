from art import logo, coffee_menu_art

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 2.00,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 3.00,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 4.00,
    }
}

# dictionary of available resources in coffee machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Functions
def check_resources(order):
    """Subtracts ingredients in customer order from available resources in resources dict. Advises customer if not enough available ingredients. Return remaining resources.
    """
    global resources
    ingredients = MENU[order]["ingredients"]
    for ingredient in ingredients:
        ingredient_resources = resources[ingredient] - MENU[order]["ingredients"][ingredient]
        # print(f"resources ingredient: {resources[ingredient]} - MENU[order]['ingredients'][ingredient]: {MENU[order]['ingredients'][ingredient]}")
        if ingredient_resources < 0:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
        else:
            resources[ingredient] = ingredient_resources
    return resources


def deposit_coins():
    print("Please deposit coins for payment.\n")
    total_deposited = int(input("How many quarters? ")) * 0.25
    total_deposited += int(input("How many dimes? ")) * 0.10
    total_deposited += int(input("How many nickels? ")) * 0.05
    total_deposited += int(input("How many pennies? ")) * 0.01
    return total_deposited


def process_payment(menu_item_cost):
    global revenue
    change = 0
    money_deposited = deposit_coins()
    if money_deposited >= menu_item_cost:
        change = f'{money_deposited - menu_item_cost:.2f}'
        print(f"\nYou deposited ${money_deposited: .2f}\nYour change is ${change}\n")
        revenue += menu_item_cost
    else:
        print("That's not enough money.\n Coins returned below.")
        return False
    return revenue

def get_report(resources, total_money):
    '''Returns remaining coffee ingredients and total revenue for drinks dispensed.
    '''
    print(f"\nRemaining Resources:\nWater: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\n")
    print(f"Total Revenue: ${total_money:.2f}.\n")


# Program
print(logo, "\n")
print(coffee_menu_art)

revenue = 0

coffee_machine_on = True
while coffee_machine_on:

    print("Espresso $2.00 / Latte $3.00 / Cappuccino $4.00\n")

    # 1. Take customer order
    coffee_order = input("What would you like?  ").lower()
    if coffee_order == 'off':
        coffee_machine_on = False
    elif coffee_order == 'report':
        get_report(resources, revenue)
    else:
        cost = MENU[coffee_order]["cost"]
        resources = check_resources(coffee_order)
        if resources:
            total_money_deposited = process_payment(cost)
            if revenue:
                print(f"Here is your {coffee_order}. Enjoy!\n")
            else:
                coffee_machine_on = False
        else:
            coffee_machine_on = False

        # 2. Check ingredients of coffee order and remaining resources
        # 3. Take payment
        # 4. Get a report of resources remaining after making coffee and total money collected by customer.


#######################Program Requirements########################
'''
Coffee Machine Program Requirements
1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
    a. Check the user’s input to decide what to do next.
    b. The prompt should show every time action has completed, e.g. once the drink is
    dispensed. The prompt should show again to serve the next customer.
2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
    the machine. Your code should end execution when this happens.
3. Print report.
    a. When the user enters “report” to the prompt, a report should be generated that shows
    the current resource values. e.g.
        Water: 100ml
        Milk: 50ml
        Coffee: 76g
        Money: $2.5
4. Check resources sufficient?
    a. When the user chooses a drink, the program should check if there are enough
    resources to make that drink.
    b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
    not continue to make the drink but print: “ Sorry there is not enough water. ”
    c. The same should happen if another resource is depleted, e.g. milk or coffee.
5. Process coins.
    a. If there are sufficient resources to make the drink selected, then the program should
    prompt the user to insert coins.
    b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
    pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
6. Check transaction successful?
    a. Check that the user has inserted enough money to purchase the drink they selected.
        E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
        program should say “ Sorry that's not enough money. Money refunded. ”.
    b. But if the user has inserted enough money, then the cost of the drink gets added to the
    machine as the profit and this will be reflected the next time “report” is triggered. E.g.
        Water: 100ml
        Milk: 50ml
        Coffee: 76g
        Money: $2.5
    c. If the user has inserted too much money, the machine should offer change.
        E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
        places.
7. Make Coffee.
    a. If the transaction is successful and there are enough resources to make the drink the
    user selected, then the ingredients to make the drink should be deducted from the
    coffee machine resources.
        E.g. report before purchasing latte:
        Water: 300ml
        Milk: 200ml
        Coffee: 100g
        Money: $0
    Report after purchasing latte:
        Water: 100ml
        Milk: 50ml
        Coffee: 76g
        Money: $2.5
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
    latte was their choice of drink.
'''
#######################Program Notes###############################

# x = 2606.89579999999
# print(f'{x:.2f}') #this code formats to round float to two decimal places and include 0 at end
# change = f'{total_money - menu_item_cost:.2f}'
# total_money_deposited = f'{total_money_deposited:.2f}'


#######################Future improvements#########################
# create a function to update a changing MENU dict to print the menu. The following isn't complete/may not work
# menu_keys_list = list(MENU)
# # print(menu_keys_list)
# coffee_menu = []
# for menu_items in menu_keys_list:
#     menu_caps = menu_items.title()
#     coffee_menu.append(menu_caps)
# cost_coffee_menu = list(MENU)

# print(f"{coffee_menu[0]} {MENU[0][1]}")