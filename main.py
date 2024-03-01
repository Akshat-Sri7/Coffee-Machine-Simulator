from menu import MENU

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def show_report():
    print(f"Water: {resources['water']}ml")
    print(f"MIlk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money : ${profit}")


def check_resources(order_ingredients):
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources[ingredient]:
            print(f"There's not enough {ingredient}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    quart = int(input("How many quarters : ")) * 0.25
    dimes = int(input("How many dimes : "))  * 0.1
    nick = int(input("How many Nickles : ")) * 0.05
    penn = int(input("How many Pennies : ")) * 0.01
    return quart+dimes+nick+penn


def check_transaction(received_amt, drink_cost, drink):
    if received_amt >= drink_cost:
        change = round((received_amt - drink_cost), 2)
        print(f"Here's the ${change} change")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money to make a {drink}. Money Refunded!")
        return False


def make_coffee(order_ingredients, drink):
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here's your {drink} ☕...Enjoy!")


def machine():
    global coins
    end = False
    while not end:
        coffee = input("What would you like (espresso/latte/cappuccino) ?: ")
        if coffee == 'off':
            break
        if coffee == 'report':
            show_report()

        drink = MENU[coffee]
        if check_resources(drink['ingredients']):
            coins = process_coins()
            if check_transaction(coins, drink['cost'], coffee):
                make_coffee(drink['ingredients'], coffee)


machine()