from fibonacci.fibonacci import fib


def test_fib_0_is_0_edge_case():
    assert fib(0) == 0


def test_fib_1_is_1_edge_case():
    assert fib(1) == 1


def test_fib_for_10():
    assert fib(10) == 55


def test_fib_for_12():
    assert fib(12) == 144


def test_fib_for_20():
    assert fib(20) == 6765

