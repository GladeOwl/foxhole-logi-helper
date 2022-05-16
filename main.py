import json

data = json.load(open('./data/data.json', 'r', encoding='utf-8'))

class Order():
    def __init__(self, name: str, amount: float, mpf: bool):
        self.name = name
        self.item = data['items'][name]
        self.amount = amount
        self.mpf = mpf
        self.status = True
        self.total_mats = None
        
        if self.mpf:
            self.calcuate_mpf()
        else:
            self.calculate_factory()

    def calculate_factory(self):
        if self.item["Type"] == "Vehicle" or self.item["Type"] == "Shippable":
            print("Cannot build Vehicles or Shippables in Factory, please select MPF.")
            self.status = False
            return
        
        self.total_mats = {
            "Bmats" : self.item['Bmats'] * self.amount,
            "Rmats" : self.item['Rmats'] * self.amount,
            "Emats" : self.item['Emats'] * self.amount,
            "HEmats" : self.item['HEmats'] * self.amount
        }

    def calcuate_mpf(self):
        if self.item["Type"] != "Vehicle" and self.item["Type"] != "Shippable" and self.amount < 3:
            print("Cannot build less than 3 crates of items.")
            self.status = False
            return

        if self.item["Type"] == "Medical" or self.item["Type"] == "Utility":
            print("Cannot build Medical and Utilities in MPF, please select Factory.")
            self.status = False
            return

        if self.name == 'Warhead':
            print('You crazy fool! Mass producing Warheads?! Get outta here!')
            self.status = False
            return

        max_mpf_queue = 9 if not self.item["Type"] == "Vehicle" or self.item["Type"] == "Shippable" else 5
        place_in_queue = 1
        starting_discount = 10
        current_discount = 10
        discount_increment = 10
        max_discount = 50
        
        bmats = 0
        rmats = 0
        emats = 0
        hemats = 0

        for count in range(self.amount):
            if (place_in_queue > max_mpf_queue):
                place_in_queue = 1
                current_discount = starting_discount

            bmats += self.calculate_discounted_amount(self.item['Bmats'], current_discount, self.item['Type'])
            rmats += self.calculate_discounted_amount(self.item['Rmats'], current_discount, self.item['Type'])
            emats += self.calculate_discounted_amount(self.item['Emats'], current_discount, self.item['Type'])
            hemats += self.calculate_discounted_amount(self.item['HEmats'], current_discount, self.item['Type'])

            if (current_discount < max_discount): 
                current_discount += discount_increment
            place_in_queue += 1
        
        self.total_mats = {
            "Bmats" : bmats,
            "Rmats" : rmats,
            "Emats" : emats,
            "HEmats" : hemats
        }
    
    def calculate_discounted_amount(self, amount, discount, type):
        if type == "Vehicle" or type == "Shippable":
            amount *= 3
        return amount - ((discount * amount) / 100)
        
# NOTE: Factory orders require a min of 3 crates in the MPF
# NOTE: MPF production becomes shorter for each extra item queued
# NOTE: If the factory has 25 queued orders (meaning it's full), the production speed increases by 15 times for item crates and 12.5 times for vehicles and shippables

new_order = Order("Green Ash Grenade", 9, True)
print(new_order.total_mats)