class Dish:

    quantity = 0

    def __init__(self, name, cost, short_arg, long_arg):
        self.name = name
        self.cost = cost
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
