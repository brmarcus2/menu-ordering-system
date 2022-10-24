import argparse
from breakfast import Breakfast
from lunch import Lunch
from dinner import Dinner
from meal import CustomException


class Order():
    def __init__(self, meal, selections):
        # no error handling here because already ran through validate_args
        #parse the selections into a list
        if (selections is None):
            self.selections = []
        else:
            self.selections = list(map(int, selections.split(",")))

        #turn input selection into corresponding class
        meal_dict = {"Breakfast": Breakfast, "Lunch": Lunch, "Dinner": Dinner}
        self.meal = meal_dict[meal](self.selections)


    def take_order(self):
        self.meal.take_order()

def parse_order_args():
    parser = argparse.ArgumentParser(description='Parse the order. ')
    parser.add_argument('meal', type=str, help = 'the meal being ordered')
    parser.add_argument('selections', type=str, help='the selected items for the meal', nargs='?', default = None)
    args = parser.parse_args()
    if validate_args(args):
        return args

def validate_args(args):
    validate_meal(args.meal)
    validate_selections(args.selections, args.meal)
    return True

def validate_meal(meal):
    if meal not in ["Breakfast", "Lunch", "Dinner"]:
        raise CustomException("The only meals available are Breakfast, Lunch, and Dinner")

def validate_selections(selections, meal):
    valid_sel_dict = { "Breakfast": [1,2,3], "Lunch":[1,2,3], "Dinner": [1,2,3,4]}
    if selections == None:
        return
    try:
        selections_list = selections.split(",")
        for sel in selections_list:
            s_int = int(sel)
            if s_int not in valid_sel_dict[meal]:
                raise Exception
    except:
        raise CustomException(f"The only order options for {meal} are {valid_sel_dict[meal]} separated by commas")


if __name__ == "__main__":
    try:
        arguments = parse_order_args()
        Order(arguments.meal, arguments.selections).take_order()
    except CustomException as e:
        print(f"Unable to process: {e.args[0]}")

