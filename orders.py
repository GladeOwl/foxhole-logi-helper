import json
import math

with open("./data/data.json", "r", encoding="utf-8") as dataFile:
    data = json.load(dataFile)


class OrderEntry(dict):
    """A class for holding a singular order entry"""

    def __init__(self, name: str, amount: int, cost: int) -> None:
        super(OrderEntry, self).__init__(self, name = name, amount = amount, cost = cost)


class TotalMats(dict):
    """Dictionary for storing total required materials"""

    def __init__(self, bmats: int = 0, rmats: int = 0, emats: int = 0, hemats: int = 0) -> None:
        super(TotalMats, self).__init__(self, Bmats = bmats, Rmats = rmats, Emats = emats, HEmats = hemats)


class Order:
    """Class for calculating an order"""

    def __init__(self, name: str, amount: float):
        self.name = name
        self.item = data["items"][name]
        self.type = self.item["Type"]
        self.amount = amount
        self.total_mats: TotalMats = TotalMats()

    def calculate_factory(self):
        """Calculate an orders cost in factory mode"""
        if self.type in ("Vehicle", "Shippable"):
            raise TypeError(f"Cannot build {self.name} in Factory, please select MPF.")

        for resource in self.total_mats:
            self.total_mats[resource] = self.item[resource] * self.amount
    
        return self.total_mats

    def calcuate_mpf(self):
        """Calculate an orders cost in manufacturing mode"""
        if self.type != "Vehicle" and self.type != "Shippable" and self.amount < 3:
            raise TypeError("Cannot build less than 3 crates of items.")

        if self.type in ("Medical", "Utility"):
            raise TypeError(f"Cannot build {self.name} in MPF, please select Factory.")

        if self.name == "Warhead":
            raise TypeError("You crazy fool! Mass producing Warheads?! Get outta here!")

        max_mpf_queue = 9 if not self.type == "Vehicle" or self.type == "Shippable" else 5
        place_in_queue = 1
        starting_discount = 10
        current_discount = 10
        discount_increment = 10
        max_discount = 50
        count = 0

        while count < self.amount:
            if place_in_queue > max_mpf_queue:
                place_in_queue = 1
                current_discount = starting_discount
            for resource in self.total_mats:
                self.total_mats[resource] += self.calculate_discounted_amount(
                    self.item[resource], current_discount, self.type
                )

            if current_discount < max_discount:
                current_discount += discount_increment
            
            place_in_queue += 1
            count += 1
        
        return self.total_mats

    def calculate_discounted_amount(self, amount, discount, type):
        """Function to calculate a discount in certain types"""
        if type in ("Vehicle", "Shippable"):
            amount *= 3
        return math.floor(amount - ((discount * amount) / 100))


def handle_orders(orders):
    """This is named wrong"""
    order_data = {"total_mats": TotalMats(), "orders": []}
    for order in orders:
        cost: TotalMats = None
        if order["mpf"]:
            cost = Order(order["name"], order["amount"]).calcuate_mpf()
        else:
            cost = Order(order["name"], order["amount"]).calculate_factory()
        
        for resource in order_data["total_mats"]:
            order_data["total_mats"][resource] += cost[resource]

        order_data["orders"].append(OrderEntry(order["name"], order["amount"], cost))

    return order_data


# NOTE: Factory orders require a min of 3 crates in the MPF
# NOTE: MPF production becomes shorter for each extra item queued
# NOTE: If the factory has 25 queued orders (meaning it's full), the production speed increases by 15 times for item crates and 12.5 times for vehicles and shippables #type: ignore

# new_order = Order("AP/RPG", 3, True)
# print(new_order.total_mats)
