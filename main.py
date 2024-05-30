from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drinks_list = Menu()
report = CoffeeMaker()
profit = MoneyMachine()


machine_on = True

while machine_on:

    user_choice = input(f"What would you like? ({drinks_list.get_items()}): ").lower()

    if user_choice == "report":
        report.report()
        profit.report()
    elif user_choice == "off":
        machine_on = False
    elif not drinks_list.find_drink(user_choice):
        pass




