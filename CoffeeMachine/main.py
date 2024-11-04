# Define the menu with coffee types and their required ingredients
menu = {
    "espresso": {
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "price": 1.5
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "price": 2.5
    },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "price": 3.0
    }
}

# Define initial resources
resources = {
    "water": 300,  # in ml
    "milk": 200,   # in ml
    "coffee": 100, # in grams
    "money": 0.0   # in dollars
}

# Define the function to print the report
def print_report():
    print("\nMachine Report:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

# Function to check resource sufficiency
def is_resource_sufficient(coffee_type):
    ingredients = menu[coffee_type]
    
    if ingredients["water"] > resources["water"]:
        print("Sorry, there is not enough water.")
        return False
    if ingredients["milk"] > resources["milk"]:
        print("Sorry, there is not enough milk.")
        return False
    if ingredients["coffee"] > resources["coffee"]:
        print("Sorry, there is not enough coffee.")
        return False
    
    return True

# Function to process coins
def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))  # Each quarter is $0.25
    dimes = int(input("How many dimes? "))        # Each dime is $0.10
    nickels = int(input("How many nickels? "))    # Each nickel is $0.05
    pennies = int(input("How many pennies? "))    # Each penny is $0.01

    # Calculate the total amount
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total

# Main function for the coffee machine
def coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino/report/off): ").lower()

        if choice in menu:
            if is_resource_sufficient(choice):
                # Get the price of the selected coffee
                drink_price = menu[choice]["price"]
                print(f"The price of a {choice} is ${drink_price}.")
                
                # Process coins and check if the payment is sufficient
                payment = process_coins()
                if payment >= drink_price:
                    # Calculate change if payment is more than the price
                    change = round(payment - drink_price, 2)
                    print(f"Transaction successful. Here is your change: ${change}")
                    
                    # Deduct resources and add money to the machine's total
                    resources["water"] -= menu[choice]["water"]
                    resources["milk"] -= menu[choice]["milk"]
                    resources["coffee"] -= menu[choice]["coffee"]
                    resources["money"] += drink_price
                    print(f"Your {choice} is ready. Enjoy!")
                else:
                    print("Sorry, that's not enough money. Money refunded.")
        
        elif choice == "report":
            print_report()
        
        elif choice == "off":
            print("Turning off the coffee machine. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please choose espresso, latte, cappuccino, report, or type 'off' to turn off the machine.")
        
        print("\nReady for the next customer.")

# Run the coffee machine function
coffee_machine()
