from meal import Meal, Course

class Lunch(Meal):
    def populate_dict(self):
        self.order_dict = { 1: "Sandwich", 2 : "Chips", 3 : "Soda"}

    # overriding match_side to allow multiple sides
    def match_side(self):
        self.ordered[Course.Side] = self.order_dict[2]
        count_side = self.selections.count(2)
        if count_side > 1:
            self.ordered[Course.Side] = self.order_dict[2] + f"({count_side})"

    def match_selections(self):
        self.match_main(self.order_dict[1])
        self.match_side()
        self.match_drink(self.order_dict[3])