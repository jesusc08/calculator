from calculator import add, subtract, multiply, divide
import pytest

def test_add():
	assert add(2, 3) == 5
def test_divide():
	assert divide(6, 2) == 3
def test_multiply():
	assert multiply(5, 7) == 35
def test_subtract():
	assert subtract(9, 5) == 4
def test_divide_uneven():
	# Arrange
	a, b = 5, 2
	# Act
	result = divide(a, b)
	# Assert
	assert result == 2.5
def test_add_uneven():
# Arrange
	a, b = -9, -3
	# Act
	result = add(a, b)
	# Assert
	assert result == -12
@pytest.mark.parametrize("a, b, expected", [
(2, 3, 5), (-2, -3, -5), (0, 0, 0),
])
def test_add_many(a, b, expected):
	assert add(a, b) == expected
