MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    profit = resources["money"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: {profit}$")


def coin_checker():
    print("please insert coins.")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


def espresso_maker():
    if resources["water"] >= MENU["espresso"]["ingredients"]["water"]:
        if resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
            money = coin_checker()
            if money < MENU["espresso"]["cost"]:
                print("sorry that\'s not enough money, money refunded.")
            else:
                if money > MENU["espresso"]["cost"]:
                    change = money - MENU["espresso"]["cost"]
                    change = round(change, 2)
                    print(f"Here is {change}$ in change")
                resources["money"] += MENU["espresso"]["cost"]
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                print("Here\'s your espresso, enjoy!")
        else:
            print("sorry coffee not enough!")
    else:
        print("sorry water not enough!")


def latte_maker():
    if resources["water"] >= MENU["latte"]["ingredients"]["water"]:
        if resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
            if resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
                money = coin_checker()
                if money < MENU["latte"]["cost"]:
                    print("sorry that\'s not enough money, money refunded.")
                else:
                    if money > MENU["latte"]["cost"]:
                        change = money - MENU["latte"]["cost"]
                        change = round(change, 2)
                        print(f"Here is {change}$ in change")
                    resources["money"] += MENU["latte"]["cost"]
                    resources["water"] -= MENU["latte"]["ingredients"]["water"]
                    resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                    resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                    print("Here\'s your latte, enjoy!")
            else:
                print("sorry milk not enough!")
        else:
            print("sorry coffee not enough!")
    else:
        print("sorry water not enough!")


def cappuccino_maker():
    if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"]:
        if resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
            if resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
                money = coin_checker()
                if money < MENU["cappuccino"]["cost"]:
                    print("sorry that\'s not enough money, money refunded.")
                else:
                    if money > MENU["cappuccino"]["cost"]:
                        change = money - MENU["cappuccino"]["cost"]
                        change = round(change, 2)
                        print(f"Here is {change}$ in change")
                    resources["money"] += MENU["cappuccino"]["cost"]
                    resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                    resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                    resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                    print("Here\'s your cappuccino, enjoy!")
            else:
                print("sorry milk not enough!")
        else:
            print("sorry coffee not enough!")
    else:
        print("sorry water not enough!")


while True:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "espresso":
        espresso_maker()
    elif order == "latte":
        latte_maker()
    elif order == "cappuccino":
        cappuccino_maker()
    elif order == "off":
        break
    elif order == "report":
        report()
    else:
        print("Wrong input try again!")
