import math_func
import pytest
import sys


# unit tests should be named with the test_ prefix to be recognized as them
@pytest.mark.number
def test_add():
    assert math_func.add(5, 4) == 9
    assert math_func.add(5) == 7
    assert math_func.add(5 + 5) == 12
    # assert math_func.add(5 + 5) == 188


# mark. are also recognized as decorators
@pytest.mark.number
def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10
    assert math_func.product(5 + 5) == 20
    # assert math_func.add(5 + 5) == 188


@pytest.mark.string
@pytest.mark.skip(reason="work in progress!!")
def test_add_strings():
    result = math_func.add('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) is str
    # assert math_func.add(5 + 5) == 188
    assert 'Hedlo' not in result


@pytest.mark.string
@pytest.mark.skipif(sys.version_info > (3, 3), reason='skip if python version is higher than 3.3')
def test_product_strings():
    print(sys.version_info)
    result = math_func.product('Hello ', 3)
    assert result == 'Hello Hello Hello '
    result = math_func.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result


# @pytest.mark.param
@pytest.mark.parametrize('x, y, result',
[
    (7, 3, 10),
    (10.5, 25.5, 36),
    (1000, 1000, 2000)
]
                         )
def test_add_param(x, y, result):
    assert math_func.add(x, y) == result
    # assert math_func.add(5 + 5) == 188
