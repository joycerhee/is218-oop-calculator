import pytest

from calculator.calculation import Add, Calculation, Subtract


def test_add_returns_sum():
    assert Add(10, 5).get_result() == 15


def test_add_stores_operands():
    calculation = Add(10, 5)
    assert calculation.a == 10
    assert calculation.b == 5


def test_add_instances_are_independent():
    first = Add(1, 2)
    second = Add(10, 20)
    assert first.get_result() == 3
    assert second.get_result() == 30


def test_add_handles_negative_and_zero():
    assert Add(-2, 3).get_result() == 1
    assert Add(0, 0).get_result() == 0


def test_subtract_returns_difference():
    assert Subtract(20, 7).get_result() == 13


def test_subtract_can_go_negative():
    assert Subtract(5, 10).get_result() == -5


def test_add_and_subtract_are_calculations():
    assert isinstance(Add(1, 2), Calculation)
    assert isinstance(Subtract(1, 2), Calculation)


def test_calculation_cannot_be_created_directly():
    with pytest.raises(TypeError):
        Calculation(1, 2)


def test_subclass_without_get_result_cannot_be_created():
    class Incomplete(Calculation):
        pass

    with pytest.raises(TypeError):
        Incomplete(1, 2)


def test_same_request_gives_each_objects_own_answer():
    calculations = [Add(10, 5), Subtract(20, 7)]
    results = [calculation.get_result() for calculation in calculations]
    assert results == [15, 13]