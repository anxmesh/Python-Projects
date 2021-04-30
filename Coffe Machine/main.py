# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
# profit = 0
#
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
# is_on = True
#
# def is_resource_sufficient(order_ingredients):
#     for item in order_ingredients:
#         if order_ingredients[item] >= resources[item]:
#             print(f"Sorry there isn't enough {item}")
#             return False
#         else:
#             return True
#
# def process_coins():
#     print("Please insert coins: ")
#     total = int(input("How many Quarters ")) * 0.25
#     total += int(input("How many dimes? ")) * 0.10
#     total += int(input("How many Nickels? ")) * 0.05
#     total += int(input("How many pennies? ")) * 0.01
#     return total
#
# def is_transaction_successful(money_received, drink_cost):
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} change!")
#         global profit
#         profit += money_received
#         return True
#     else:
#         print("Sorry that's not enough money! Money refunded. ")
#         return False
#
# def make_coffee(drink_name, order_ingredients):
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name}. ENjoy!")
#
# while is_on:
#
#     choice = input("What would you like (expresso/cappuccino/latte): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water = {resources['water']} ml")
#         print(f"Milk = {resources['milk']} ml")
#         print(f"Water = {resources['coffee']} g")
#         print(f"Money made: $ {profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cofee_list = Menu()
cofee_makers = CoffeeMaker()
money_machines = MoneyMachine()
is_on = True



while is_on:
    items = cofee_list.get_items()
    choice = input(f"What would you like ({items}) :?")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machines.report()
        cofee_makers.report()
    else:
        drink = cofee_list.find_drink(choice)
        print(drink)
        if (cofee_makers.is_resource_sufficient(drink)) and money_machines.make_payment(drink.cost):
            cofee_makers.make_coffee(drink)





