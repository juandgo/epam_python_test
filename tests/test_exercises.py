from src.epam_python_exercises import *

# Save this in a file named test_exercises.py

### --- EXERCISE 1 ---


def test_dictionary():
    d = Dictionary()
    d.newentry("Apple", "A fruit")
    assert d.look("Apple") == "A fruit"
    assert d.look("Banana") == "Can't find entry for Banana"


### --- EXERCISE 2 ---


def test_get_total():
    costs = {"socks": 5, "shoes": 60}
    assert get_total(costs, ["socks", "shoes"], 0.09) == 70.85


### --- EXERCISE 3 ---


def test_nth_char():
    assert nth_char(["yoda", "best", "has"]) == "yes"
    assert nth_char(["hello", "view", "mother"]) == "hit"
