#!/usr/bin/python3
""" Resturant prices """

import sys
import pandas as pd
import configparser
import config as global_vars
from dish import Dish
from order import Order


def calc_tax(price, tax):
    """
    returns price's tax amount
    """

    return price * tax / 100

if __name__ == '__main__':

    order = Order()

    DISHES = []

    config = configparser.ConfigParser()
    config.read(global_vars.resturant_data_file)

    TAX = config['internal-config'].getfloat('tax')

    # if the section isn't internal then make a dish object from it
    for section in config.sections():
        sec_info = config[section]
        if 'type' in sec_info and sec_info['type'] == 'dish':
            name = section
            cost = sec_info.getfloat('cost')
            long_arg = sec_info.get('long_arg')
            short_arg = sec_info.get('short_arg')
            dish = Dish(name, cost, TAX)
            dish.set_long_arg(long_arg)
            dish.set_short_arg(short_arg)
            for key in sec_info.keys():
                dish.add_info(key, sec_info[key])
            DISHES.append(dish)

    total_cost = 0

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
                order.add_dish(dish)

    # make the a list of only the ordered foods
    ordered_costs = [dish.cost for dish in order.dishes]
    ordered_names = [dish.name for dish in order.dishes]

    # calculate tax to total_cost
    total_cost += calc_tax(total_cost, TAX)

    number_of_dishes_total = 0

    # Adds a (floating point) running total as entries...
    # in total_array like so:
    #   [
    #       24.98, 30.97, 50.96
    #   ]

    total_array = []
    for dish in order.dishes:
        number_of_dishes_total += dish.quantity
        if len(total_array) == 0:
            total_array.append(dish.get_total_cost())
        else:
            total_array.append(dish.get_total_cost() + total_array[-1])

    # Formats ordered food info
    df = pd.DataFrame({'dish': ordered_names})
    df['$/dish'] = ['$' + '{0:.2f}'.format(cost) for cost in ordered_costs]
    df['#/dishes'] = [dish.quantity for dish in order.dishes]
    df['$/#/dishes'] = ['$' + '{0:.2f}'.format(dish.get_total_cost()) for dish in order.dishes]
    df['total'] = ['$' + '{0:.2f}'.format(cost) for cost in total_array]

    # Print some final info about different calculations
    print(df)
    print()
    print("All prices include TAX")
    print("${0} total".format(round(total_cost, 2)))
    print("${0} dish avg".format(round(total_cost/number_of_dishes_total, 2)))
    print("${0} dish / person avg".format(
        round(
            total_cost/number_of_dishes_total/float(config['internal-config'].getint('people')), 2)
        ))
    print("${0} / per person total".format(
        round(
            total_cost/float(config['internal-config'].getint('people')), 2)
        ))
