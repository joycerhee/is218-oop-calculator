from calculator.calculation import Add


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
