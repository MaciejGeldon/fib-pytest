import pytest
from fibonacci.fibonacci import fib


@pytest.mark.parametrize(
    'fib_index, result',
    [
        (0, 0),
        (1, 1),
        (10, 55),
        (12, 144),
        (20, 6765)
    ]
)
def test_fib_0_is_0_edge_case(fib_index, result):
    assert fib(fib_index) == result


@pytest.mark.slow
@pytest.mark.parametrize(
    'fib_index, result',
    [
        (35, 9227465),
        (38, 39088169),
        (40, 102334155)
    ]
)
def test_fibonacci_larger_indexes(fib_index, result):
    assert fib(fib_index) == result
