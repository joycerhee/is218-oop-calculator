import pytest

from calculator.calculation import Add, Subtract
from calculator.history import History


def test_new_history_is_empty():
    assert History().get_all() == []


def test_add_keeps_calculations_in_order():
    history = History()
    first = Add(10, 5)
    second = Subtract(20, 7)
    history.add(first)
    history.add(second)
    assert history.get_all() == [first, second]


def test_get_all_returns_a_copy():
    history = History()
    history.add(Add(10, 5))
    returned = history.get_all()
    returned.clear()
    assert len(history.get_all()) == 1


def test_remove_returns_the_entry_and_keeps_the_rest():
    history = History()
    first = Add(10, 5)
    second = Subtract(20, 7)
    history.add(first)
    history.add(second)
    assert history.remove(0) is first
    assert history.get_all() == [second]


def test_remove_rejects_positions_outside_the_list():
    history = History()
    history.add(Add(10, 5))
    for index in [1, 5, -1]:
        with pytest.raises(IndexError):
            history.remove(index)
    assert len(history.get_all()) == 1