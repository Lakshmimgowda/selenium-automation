import pytest

def is_even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

@pytest.mark.parametrize("n",[2,4,6,8,10,12,13])

#@pytest.mark.skip  #to skip the test case
def test_even_numbers(n):
    result = is_even_or_odd(n)
    assert result == "Even"

def test_odd_numbers(n):
    result = is_even_or_odd(n)
    assert result == "Odd"

def add(a, b):
    return a + b

@pytest.mark.parametrize("a,b,result", [(1,2,3),
                                        (2,2,4)])

def test_add(a, b, result):

    assert a+b == result
    # assert result == 5