"""
This module/object represents a Resturnat. Currently only to calculate tax
"""


class Resturant():

    """
    Resturant object:
        tax is the tax precentage, default 5
    """

    def __init__(self, tax=5.00):
        """
        initializes a resturnat
        """

        self.tax = tax

    def get_tax(self):
        """
        returns resturnant's tax
        """

        return self.tax

    def set_tax(self, new_tax):
        """
        Sets resturnat's new tax precentage to new_tax
        """

        self.tax = new_tax

    def calc_tax_on_dish(self, dish_cost):
        """
        returns (dish_cost*resturant.tax)/100
        """

        return (dish_cost*self.tax)/100
