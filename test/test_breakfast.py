from breakfast import Breakfast
from meal import Course

def test_match_drink_one_coffee():
    b = Breakfast([1,2,3])
    b.order_dict = {1: "Eggs", 2: "Toast", 3: "Coffee"}
    b.match_drink()
    assert(b.ordered[Course.Drink] == "Coffee")

def test_match_drink_many_coffee():
    b = Breakfast([1,2,3,3])
    b.order_dict = { 1: "Eggs", 2 : "Toast", 3 : "Coffee"}
    b.match_drink()
    assert(b.ordered[Course.Drink] == "Coffee(2)")

def test_match_drink_no_coffee():
    b = Breakfast([1,2])
    b.order_dict = { 1: "Eggs", 2 : "Toast", 3 : "Coffee"}
    b.match_drink()
    assert(b.ordered[Course.Drink] == "Water")