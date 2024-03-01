from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

end = False

while not end:
    choice = input(f"What would you like? ({menu.get_items()})")
    if choice == 'off':
        break
    elif choice == 'report':
        money_machine.report()
        coffee_maker.report()
        continue
    else:
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
