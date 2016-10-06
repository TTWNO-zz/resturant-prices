"""
This module uses the Dish object to hold data about different resturnat dishes.

Main Class:
    Dish object representing a dish from a resturant

    get_tax, set_tax
    get_name, set_name
    get_price, set_price
    get_quantity, set_quantity
    get_short_arg, set_short_arg
    get_long_arg, set_long_arg

    these functions are self-expanitory

    This class currently only holds data, more complicated things coming soon...
"""


class Dish:

    """
    __init__() variables:
        name is 'proper' name of dish String, default "?"
        cost is the cost of the dish, default 0.00
        tax is the tax precentage on the specific dish, default 0
        short_arg is the short UNIX argument that sets the quantity, default -<first char of name>
        long_arg is the long UNIX argument that sets the quantity, default --lowercase-name-of-dish


    override by method:
        short_arg is the short UNIX argument that sets the quantity, default -u
        long_arg is the long UNIX argument that sets the quantity, default --unknown
    """

    quantity = 0

    def __init__(self, name="?", cost=0.00, tax=0):
        self.name = name
        self.cost = cost
        self.tax = tax

        self.short_arg = '-' + name.lower()[0]
        self.long_arg = '--' + name.lower().replace(' ', '-')
        self.info = {}

    def add_info(self, key, value):
        """
        adds key value pair to info table
        """

        self.info[key] = value

    def get_info(self, key):
        """
        returns info[key]
        """

        return self.info[key]

    def get_tax_rate(self):
        """
        returns tax rate of dish
        """

        return self.tax

    def set_tax_rate(self, new_tax):
        """
        sets tax rate for dish to new_tax
        """

        self.tax = new_tax

    def get_name(self):
        """
        returns dish's proper name as string
        """

        return self.name

    def set_name(self, name):
        """
        sets dish's proper name to name
        """

        self.name = name

    def get_cost(self):
        """
        returns dish's cost as float to 2 deicimal points
        """

        return self.cost

    def set_cost(self, cost):
        """
        sets cost of dish to cost rounded to 2 deicimal point
        """

        self.cost = float(cost, 2)

    def get_sort_arg(self):
        """
        returns short UNIX argument
        """

        return self.short_arg

    def set_short_arg(self, short_arg):
        """
        sets short UNIX argument to short_arg
        """

        self.short_arg = short_arg

    def get_long_arg(self):
        """
        returns long UNIX arguments
        """

        return self.long_arg

    def set_long_arg(self, long_arg):
        """
        sets long UNIX argument to long_arg
        """

        self.long_arg = long_arg

    def get_quantity(self):
        """
        returns the amount of dishes this object represents
        """

        return self.quantity

    def set_quantity(self, quantity):
        """
        sets the quanity of dishes to quantity
        """

        self.quantity = quantity

    def get_tax(self):
        """
        retruns the calculated tax on 1 dish
        """

        return self.cost * self.tax / 100

    def get_total_cost(self, apply_tax=False):
        """
        returns cost for p w/ tax * quantity

        params:
            apply_tax, bool. if should return cost with or without tax
        """

        if apply_tax:
            return self.get_total_cost() * self.get_tax_rate/100
        return self.cost * self.quantity
