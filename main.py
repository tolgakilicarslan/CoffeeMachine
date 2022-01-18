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
water_supply = 300
milk_supply = 200
coffee_supply = 100
money_earned = 0
turn_off = False
while turn_off == False:
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    if drink == "off":
        turn_off = True
    elif drink == "report":
        print(f"Water: {water_supply} ml")
        print(f"Milk: {milk_supply} ml")
        print(f"Coffee: {coffee_supply} g")
        print(f"Money: ${money_earned}")
    else:
        ingredients = MENU[drink].get("ingredients")
        water_used = ingredients.get("water")
        milk_used = ingredients.get("milk")
        coffee_used = ingredients.get("coffee")
        cost = MENU[drink].get("cost")
        if water_used > water_supply:
            print("Sorry, there is not enough water. Money refunded")
        elif drink != "espresso" and milk_used > milk_supply:
            print("Sorry, there is not enough milk. Money refunded")
        elif coffee_used > coffee_supply:
            print("Sorry, there is not enough coffee. Money refunded")
        else:
            print(f"the {drink} costs ${cost}")
            print("Please insert coins.")
            quarters = float(input("how many quarters?: "))
            dimes = float(input("how many dimes?: "))
            nickles = float(input("how many nickles?: "))
            pennies = float(input("how many pennies?: "))
            total_money = 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies
            print(f"Total money entered: ${total_money}")
            change = round(total_money - cost, 2)
            print(f"Here is ${change} dollars in change.")
            print(f"Here is your {drink} ☕️. Enjoy!")
            water_supply -= water_used
            if drink != "espresso":
                milk_supply -= milk_used
            coffee_supply -= coffee_used
            money_earned += cost
            if drink == "off":
                turn_off = True
            elif drink == "report":
                print(f"Water: {water_supply} ml")
                print(f"Milk: {milk_supply} ml")
                print(f"Coffee: {coffee_supply} g")
                print(f"Money: ${money_earned}")







