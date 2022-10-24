import pytest
from meal import CustomException, Course
from breakfast import Breakfast
from lunch import Lunch

def test_main_and_side_no_main():
    with pytest.raises(CustomException)  as e:
        b = Breakfast([2,3])
        b.main_and_side()
        assert(e.args[0] == "Main is missing")

def test_main_and_side_no_side():
    with pytest.raises(CustomException) as e:
        b = Breakfast([1,3])
        b.main_and_side()
        assert(e.args[0] == "Side is missing")

def test_main_and_side_no_main_no_side():
    with pytest.raises(CustomException) as e:
        b = Breakfast([])
        b.main_and_side()
        assert(e.args[0] == "Main is missing, Side is missing")

def test_match_drink_no_drink():
    l = Lunch([1,2])
    l.match_drink("Soda")
    assert(l.ordered[Course.Drink] == "Water")

def test_match_drink_with_drink():
    l = Lunch([1,2,3])
    l.match_drink("Soda")
    assert(l.ordered[Course.Drink] == "Soda")

def test_match_drink_two_drink():
    with pytest.raises(CustomException) as e:
        l = Lunch([1,2,3,3])
        l.match_drink("Soda")
        assert(e.args[0] == "Soda cannot be ordered more than once")

def test_match_main():
    l = Lunch([1,2,3])
    l.match_main("Sandwich")
    assert(l.ordered[Course.Main] == "Sandwich")

def test_match_main_two_main():
    with pytest.raises(CustomException) as e:
        l = Lunch([1,1,2,3])
        l.match_main("Sandwich")
        assert(e.args[0] == "Sandwich cannot be ordered more than once")

def test_match_side():
    b = Breakfast([1,2,3])
    b.match_side("Toast")
    assert(b.ordered[Course.Side] == "Toast")

def test_match_side_two_side():
    with pytest.raises(CustomException) as e:
        b = Breakfast([1,2,2,3])
        b.match_side("Toast")
        assert(e.args[0] == "Toast cannot be ordered more than once")


def test_mail_string():
    b = Breakfast([1, 2, 3])
    b.populate_dict()
    b.match_selections()
    assert(b.get_meal_string() == f"{b.ordered[Course.Main]}, {b.ordered[Course.Side]}, {b.ordered[Course.Drink]}")