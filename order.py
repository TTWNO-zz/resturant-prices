"""Order class"""


class Order:

    """
    Class Order:

        Vars:
            dishes, list of dishes (Dish) objects

        Functions:
            get_cost() generates cost based on dishes
            add_dish(Dish) adds a dish to the dishes list
    """

    def __init__(self):
        self.dishes = []

    def get_cost(self, apply_tax=False):
        """
        returns cost of order
        """
        total_cost = 0.00
        for dish in self.dishes:
            total_cost += dish.calc_tax(apply_tax)
        return total_cost

    def add_dish(self, dish):
        """
        adds dish to order
        """
        self.dishes.append(dish)
