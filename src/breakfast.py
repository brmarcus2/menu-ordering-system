from meal import Meal, Course

class Breakfast(Meal):
    def populate_dict(self):
        self.order_dict = { 1: "Eggs", 2 : "Toast", 3 : "Coffee"}

    # override match_drink from Meal because multiple coffees are allowed
    def match_drink(self):
        if 3 not in self.selections:
            self.ordered[Course.Drink] = "Water"
        else:
            self.ordered[Course.Drink] = self.order_dict[3]
            count_coffee = self.selections.count(3)
            if count_coffee > 1:
                self.ordered[Course.Drink] = self.order_dict[3] + f"({count_coffee})"

    def match_selections(self):
        self.match_main(self.order_dict[1])
        self.match_side(self.order_dict[2])
        self.match_drink()
