#!/usr/bin/python3

import sys
import pandas as pd
from dish import Dish
import configparser

CONFIG_FILE = 'resturant-data.txt'

DISHES = []
ordered_dishes = []

config = configparser.ConfigParser()
config.read(CONFIG_FILE)
for section in config.sections():
    if 'internal-' not in section:
        dish_info = config[section]
        name = section
        cost = dish_info.getfloat('cost')
        long_arg = dish_info.get('long_arg')
        short_arg = dish_info.get('short_arg')
        dish = Dish(name, cost, short_arg, long_arg)
        DISHES.append(dish)

TAX = config['internal-config'].getfloat('tax')

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
        config['internal-config']['people'] = sys.argv[i+1]

    for dish in DISHES:
        if arg == dish.short_arg or arg == dish.long_arg or arg == dish.name:
            if len(sys.argv) > i+1 and sys.argv[i+1].isdigit():
                how_many_dishes = int(sys.argv[i+1])
            dish.set_quantity(how_many_dishes)
            total_cost += dish.get_total_cost()
            ordered_dishes.append(dish)

# make the a list of only the ordered foods
ordered_costs = [dish.cost for dish in ordered_dishes]
ordered_names = [dish.name for dish in ordered_dishes]

# calculate tax to total_cost
tax = calc_tax(total_cost, TAX)
total_cost += tax

number_of_dishes_total = 0

# Adds a (floating point) running total as entries...
# in total_array like so:
#   [
#       24.98, 30.97, 50.96
#   ]

total_array = []
for dish in ordered_dishes:
    number_of_dishes_total += dish.quantity
    if len(total_array) == 0:
        total_array.append(dish.get_total_cost())
    else:
        total_array.append(dish.get_total_cost() + total_array[-1])

# Formats ordered food info
df = pd.DataFrame({'dish': ordered_names})
df['$/dish'] = ['$' + '{0:.2f}'.format(cost) for cost in ordered_costs]
df['#/dishes'] = [dish.quantity for dish in ordered_dishes]
df['$/#/dishes'] = ['$' + '{0:.2f}'.format(dish.get_total_cost()) for dish in ordered_dishes]
df['total'] = ['$' + '{0:.2f}'.format(cost) for cost in total_array]

# Print some final info about different calculations
print(df)
print()
print("All prices include TAX")
print("${0} total".format(round(total_cost, 2)))
print("${0} dish avg".format(round(total_cost/number_of_dishes_total, 2)))
print("${0} dish / person avg".format(round(total_cost/number_of_dishes_total/float(config['internal-config'].getint('people')), 2)))
print("${0} / per person total".format(round(total_cost/float(config['internal-config'].getint('people')), 2)))
