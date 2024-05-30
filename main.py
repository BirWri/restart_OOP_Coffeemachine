from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
money = MoneyMachine()


machine_on = True

while machine_on:

    order_name = input(f"What would you like? ({menu.get_items()}): ").lower()
    order = menu.find_drink(order_name)

    if order_name == "report":
        coffeemaker.report()
        money.report()
    elif order_name == "off":
        machine_on = False

    #if not coffeemaker.is_resource_sufficient():
        #machine_on = False

        # Ask payment

        # Check payment
        # Make coffee
    #coffeemaker.make_coffee(order_name)







