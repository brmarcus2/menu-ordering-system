import pytest
from order import Order, validate_meal, validate_selections
from breakfast import Breakfast
from lunch import Lunch
from dinner import Dinner
from meal import CustomException


def test_order_match_Breakfast():
    o = Order("Breakfast", "1,2,3")
    assert isinstance(o.meal, Breakfast)

def test_order_match_Lunch():
    o = Order("Lunch", "1,2,3")
    assert isinstance(o.meal, Lunch)

def test_order_match_Dinner():
    o = Order("Dinner", "1,2,3,4")
    assert isinstance(o.meal, Dinner)

def test_validate_meal():
    with pytest.raises(CustomException) as e:
        validate_meal("nothing")
        assert(e.args[0] == "Main is missing, Side is missing")

def test_validate_selections_alpha():
    with pytest.raises(CustomException) as e:
        validate_selections("a,b", "Breakfast")
        assert(e.args[0] == "The only order options for Breakfast are [1, 2, 3] separated by commas")

def test_validate_selections_wrong_format():
    with pytest.raises(CustomException) as e:
        validate_selections("1 + 2 + 3", "Breakfast")
        assert(e.args[0] == "The only order options for Breakfast are [1, 2, 3] separated by commas")

def test_validate_selections_valid_selections():
    try:
        validate_selections("1,2,3", "Breakfast")
    except CustomException as e:
        assert False, f"validate_selections raised an exception {e}"

def test_validate_selections_wrong_numbers():
    with pytest.raises(CustomException) as e:
        validate_selections("1,4,5", "Breakfast")
        assert(e.args[0] == "The only order options for Breakfast are [1, 2, 3] separated by commas")
