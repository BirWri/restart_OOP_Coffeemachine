from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
money = MoneyMachine()

machine_on = True
while machine_on:

    order_name = input(f"What would you like? ({menu.get_items()}): ").lower()

    if order_name == "report":
        coffeemaker.report()
        money.report()
    elif order_name == "off":
        machine_on = False
    else:
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









