from meal import Meal, Course, CustomException

class Dinner(Meal):

    def take_order(self):
        self.check_dessert()
        super().take_order()

    def check_dessert(self):
        if 4 not in self.selections:
            self.error = ["Dessert is missing"]
        else:
            self.error = []

    def populate_dict(self):
        self.order_dict = { 1: "Steak", 2 : "Potatoes", 3 : "Wine", 4 : "Cake"}

    # overriding match drink because water is additional
    def match_drink(self):
        if self.selections.count(3) > 1:
            raise CustomException(f"{self.order_dict[Course.Drink]} cannot be ordered more than once")
        if 3 not in self.selections:
            self.ordered[Course.Drink] = "Water"
        else:
            self.ordered[Course.Drink] = f"{self.order_dict[3]}, Water"

    def match_dessert(self):
        if self.selections.count(4) > 1:
            raise CustomException(f"{self.order_dict[4]} cannot be ordered more than once")
        self.ordered[Course.Dessert] = self.order_dict[4]

    def match_selections(self):
        self.match_main(self.order_dict[1])
        self.match_side(self.order_dict[2])
        self.match_drink()
        self.match_dessert()

    def get_meal_string(self):
        return (super().get_meal_string() + ", " + self.ordered[Course.Dessert])