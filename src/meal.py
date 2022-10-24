from abc import ABC, abstractmethod
from enum import Enum

# using a custom exception to be able to control the error message behavior
class CustomException(Exception):
    pass

# using enums to make sure there aren't string matching issues in meal logic
class SelectedMeal(Enum):
    Breakfast = 1
    Lunch = 2
    Dinner = 3

class Course(Enum):
    Main = 1
    Side = 2
    Drink = 3
    Dessert = 4

class Meal(ABC):
    def __init__(self, selections, error = []):
        self.selections = selections
        self.ordered = {}
        self.error = error

    def take_order(self):
        self.main_and_side()
        self.populate_dict()
        self.match_selections()
        self.print_order()

    # filling in the dictionary with the menu is specific to the subclass
    @abstractmethod
    def populate_dict(self):
        pass

    #each order must contain a main and a side
    def main_and_side(self):
        if 1 not in self.selections:
            self.error.append("Main is missing")
        if 2 not in self.selections:
            self.error.append("Side is missing")
        if len(self.error) > 0:
            error_string = ", ".join(self.error)
            raise CustomException(error_string)


    # filling in the order from the numbers is abstract to allow the name of the order to be passed into the
    #   relevant match method, which allows error handling to be specific while keeping match methods in Meal
    @abstractmethod
    def match_selections(self):
        pass


    # base drink behavior - water if no drink is ordered, and only one drink can be ordered
    def match_drink(self, drink_name):
        if 3 not in self.selections:
            self.ordered[Course.Drink] = "Water"
        else:
            if self.selections.count(3) > 1:
                raise CustomException(f"{drink_name} cannot be ordered more than once")
            else:
                self.ordered[Course.Drink] = drink_name

    # base main behavior - only one can be ordered
    def match_main(self, main_name):
        if self.selections.count(1) > 1:
            raise CustomException(f"{main_name} cannot be ordered more than once")
        self.ordered[Course.Main] = main_name

    # base side behavior - only 1 can be ordered
    def match_side(self, side_name):
        if self.selections.count(2) > 1:
            raise CustomException(f"{side_name} cannot be ordered more than once")
        self.ordered[Course.Side] = side_name

    # customizing printing to control the format and order
    def print_order(self):
        print(self.get_meal_string())

    # separating out getting the string to print to make it easy to add on the dessert for dinner
    def get_meal_string(self):
        return f"{self.ordered[Course.Main]}, {self.ordered[Course.Side]}, {self.ordered[Course.Drink]}"
