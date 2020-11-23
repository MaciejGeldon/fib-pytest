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
