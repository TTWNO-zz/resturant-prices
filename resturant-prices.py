#!/usr/bin/python3

import sys
import pandas as pd

config = {}

class Dish:

    quantity = 0

    def __init__(self, cost, name, short_arg, long_arg):
        self.cost = cost
        self.name = name
        self.short_arg = short_arg
        self.long_arg = long_arg

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def get_cost(self):
        return self.cost
    def set_cost(self, cost):
        self.cost = cost

    def get_sort_arg(self):
        return self.short_arg
    def set_short_arg(self, short_arg):
        self.short_arg = short_arg

    def get_long_arg(self):
        return self.long_arg
    def set_long_arg(self, long_arg):
        self.long_arg = long_arg

    def get_quantity(self):
        return self.quantity
    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_total_cost(self):
        return self.quantity * self.cost

DISHES = []
with open('dimsum-data.txt') as f:
    for line in f:
        if line[0] == 'D':
            args = line.rstrip('\n').split(':')
            cost = float(args[1])
            name = args[2]
            long_arg = name.lower()
            short_arg = name.lower()[0]

            if len(args) > 3:
                long_arg = args[3]
            if len(args) > 4:
                short_arg = args[4]

            dish = Dish(cost, name, short_arg, long_arg)
            DISHES.append(dish)
        elif line[0] == 'C':
            type_option = line.split(':')[1]
            key, value = line.split(':')[2].split('=')
            if type_option == 'float':
                value = float(value)
            elif type_option == 'int':
                value = int(value)
            elif type_option == 'str':
                value = str(value)
            config[key] = value


COSTS = [dish.cost for dish in DISHES]

LONG_NAMES = [dish.long_arg for dish in DISHES]

SHORT_NAMES = [dish.short_arg for dish in DISHES]

PROPER_NAMES = [dish.name for dish in DISHES]

total_cost = 0

def calc_tax(t, p):
    """
    Calculates tax on t for precent p

    returns (t)*p/100
    """
    return t * p/100

for i in range(len(sys.argv)):
    arg = sys.argv[i]
    how_many_dishes = 1

    if arg == '-h' or arg == '--help':
        print("Usage: ")
        print("python3 dimsum.py [--size | -s] [number of dishes(default 1)]")
    elif arg == '-p' or arg == '--people':
        config['people'] = sys.argv[i+1]

    for dish in DISHES:
        if arg == dish.short_arg or arg == dish.long_arg:
            if len(sys.argv) > i+1 and sys.argv[i+1].isdigit():
                how_many_dishes = int(sys.argv[i+1])
            dish.set_quantity(how_many_dishes)
            total_cost += dish.get_total_cost()

tax = calc_tax(total_cost, config['tax'])
total_cost += tax

number_of_dishes_total = 0

total_array = []
for dish in DISHES:
    number_of_dishes_total += dish.quantity
    if len(total_array) == 0:
        total_array.append(dish.get_total_cost())
    else:
        total_array.append(dish.get_total_cost() + total_array[-1])

df = pd.DataFrame({'size': PROPER_NAMES})
df['$/dish'] = ['$' + '{0:.2f}'.format(cost) for cost in COSTS]
df['#/dishes'] = [dish.quantity for dish in DISHES]
df['$/#/dishes'] = ['$' + '{0:.2f}'.format(dish.get_total_cost()) for dish in DISHES]
df['total'] = ['$' + '{0:.2f}'.format(cost) for cost in total_array]

print(df)
print()
print("All prices include TAX")
print("${0} total".format(round(total_cost, 2)))
print("${0} dish avg".format(round(total_cost/number_of_dishes_total, 2)))
print("${0} dish / person avg".format(round(total_cost/number_of_dishes_total/float(config['people']), 2)))
print("${0} / per person total".format(round(total_cost/float(config['people']), 2)))
