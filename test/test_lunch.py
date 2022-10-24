from lunch import Lunch
from meal import Course

def test_match_side_one_side():
    l = Lunch([1,2,3])
    l.order_dict = { 1: "Sandwich", 2 : "Chips", 3 : "Soda"}
    l.match_side()
    assert(l.ordered[Course.Side] == "Chips")

def test_match_side_many_sides():
    l = Lunch([1,2,2,3])
    l.order_dict = { 1: "Sandwich", 2 : "Chips", 3 : "Soda"}
    l.match_side()
    assert(l.ordered[Course.Side] == "Chips(2)")
