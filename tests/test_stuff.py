from hypothesis.testdecorators import given
import pytest

# Examples of example-based testing
def test_list_append_associative_example1():
    x, y, z = [2], [3, 4, 5], [6, 7]
    assert (x + y) + z == x + (y + z)

def test_list_append_associative_example2():
    x, y, z = [2, 3], [], [6, 7]
    assert (x + y) + z == x + (y + z)

@pytest.mark.parametrize (("x", "y", "z"), [
    ([2], [3, 4, 5], [6, 7]),
    ([2, 3], [], [6, 7])
])
def test_list_append_associative_parametrized(x, y, z):
    assert (x + y) + z == x + (y + z)
    
# Examples of decorator-based hypothesis testing.
@given ([int], [int], [int])
def test_list_append_associative(x, y, z):
    assert (x + y) + z == x + (y + z)

@given (int, int)
def test_multiply_then_divide_is_same(x, y):
    assert (x * y) / y == x

# Shows that Python has arbitrary precision int arithmetic, unlike
# C and Java whose ints will overflow.
@given (int, int)
def test_multiply_nonzero_then_divide_is_same(x, y):
    if y != 0:
        assert (x * y) / y == x
