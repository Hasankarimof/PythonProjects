from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coffee_machine():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")

        if choice == "off":
            print("Turning off the coffee machine...")
            break
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if drink:
                if coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)
                else:
                    print("Sorry, there are not enough resources to make that drink.")
            else:
                print("Sorry, we don't have that drink.")

coffee_machine()