""" GladeOwl's Foxhole Logistic Helper Script """
import json
import orders


# NOTE: Make it able to do the orders in Phases.
# Meaning amount more than the max factory amount will be calculated as part of a different phase.
# Simplifying trips.

# INPUT: 1. Orders, 2. is it MPF, 3. Vehicle (optional, will default to Truck)

# 1. Input a list of items along with the amount for each.
# 2. Create a list of the inputted items, along with the materials required.
# 3.

####
# TEST
# list of orders
order_list = []
order_list.append({"name": "7.62mm", "amount": 10, "mpf": True})
order_list.append({"name": "Dusk ce.III", "amount": 6, "mpf": True})
order_list.append({"name": "HC-2 Scorpion", "amount": 3, "mpf": True})
order_list.append({"name": "UV-24 Icarus", "amount": 7, "mpf": True})

orders_data = orders.handle_orders(order_list)

with open("output.json", "w", encoding="utf-8") as jsonf:
    jsonf.write(json.dumps(orders_data, indent=4))
