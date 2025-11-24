from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

item_menu = Menu()
barista = CoffeeMaker()
accountant = MoneyMachine()
while True:

    choice=input(f"What would you like? ({item_menu.get_items()}): ").lower()

    if choice=="report":
        barista.report()
        accountant.report()

    elif choice=="off":
        exit()
    else:
        item = item_menu.find_drink(choice)
        if barista.is_resource_sufficient(item) and accountant.make_payment(item.cost):
            barista.make_coffee(item)








