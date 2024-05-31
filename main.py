from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
money = MoneyMachine()

machine_on = True
while machine_on:
    # Ask user for their choice
    order_name = input(f"What would you like? ({menu.get_items()}): ").lower()

    # prints the available resources of the coffee machine or turn the machine off
    if order_name == "report":
        coffeemaker.report()
        money.report()
    elif order_name == "off":
        machine_on = False
    else:
        # Variable to store the drinks attributes. If no drink exist, ask for a new drink
        # input. If drink exist and the resources are enough, and the user provides enough
        # money - make the drink.
        order = menu.find_drink(order_name)

        if not order:
            pass
        elif coffeemaker.is_resource_sufficient(order):
            # Ask payment
            payment = money.make_payment(order.cost)
            if payment:
                # Make coffee
                coffeemaker.make_coffee(order)
        else:
            machine_on = False









