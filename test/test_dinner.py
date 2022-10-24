import pytest
from meal import CustomException, Course
from dinner import Dinner

def test_match_dessert_no_dessert():
    d = Dinner([1,2,3])
    d.order_dict = {1: "Steak", 2: "Potatoes", 3: "Wine", 4: "Cake"}
    d.check_dessert()
    assert(d.error == ["Dessert is missing"])

def test_match_drink_no_drink():
    d = Dinner([1,2,4])
    d.order_dict = {1: "Steak", 2: "Potatoes", 3: "Wine", 4: "Cake"}
    d.match_drink()
    assert(d.ordered[Course.Drink] == "Water")

def test_match_drink_with_drink():
    d = Dinner([1,2,3,4])
    d.order_dict = {1: "Steak", 2: "Potatoes", 3: "Wine", 4: "Cake"}
    d.match_drink()
    assert(d.ordered[Course.Drink] == "Wine, Water")

def test_match_dessert():
    d = Dinner([1,2,3,4])
    d.order_dict = {1: "Steak", 2: "Potatoes", 3: "Wine", 4: "Cake"}
    d.match_dessert()
    assert(d.ordered[Course.Dessert] == d.ordered[Course.Dessert])

def test_match_dessert_two_dessert():
    with pytest.raises(CustomException) as e:
        d = Dinner([1,2,3,4,4])
        d.order_dict = {1: "Steak", 2: "Potatoes", 3: "Wine", 4: "Cake"}
        d.match_dessert()
        assert(e.args[0] == "Cake cannot be ordered more than once")

def test_mail_string():
    d = Dinner([1, 2, 3, 4])
    d.populate_dict()
    d.match_selections()
    assert(d.get_meal_string() == f"{d.ordered[Course.Main]}, {d.ordered[Course.Side]}, {d.ordered[Course.Drink]}, {d.ordered[Course.Dessert]}")