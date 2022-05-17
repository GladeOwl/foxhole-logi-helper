import json
import math

# NOTE: Make it able to do the orders in Phases. Meaning amount more than the max factory amount will be calculated as part of a different phase. Simplifying trips.

data = json.load(open('./data/data.json', 'r', encoding='utf-8'))

class Trip():
    def __init__(self):
        pass