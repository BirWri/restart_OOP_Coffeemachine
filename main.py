from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drinks_list= Menu()
user_choice = input(f"What would you like? ({drinks_list.get_items()}): ").lower()


