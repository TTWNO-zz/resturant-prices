import sys
import configparser
import config as global_vars

config = configparser.ConfigParser()
config.read(global_vars.resturant_data_file)

dish_num = 1
for section in config.sections():
    if 'internal-' not in section:
        print("Dish {0} \"{1}\"".format(dish_num, section))
        for key in config[section]:
            print('    {0} = {1}'.format(key, config[section][key]))
        print()
        dish_num += 1
