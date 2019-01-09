import pytest

def test_assertInt():
    assert 3 == 3

def test_assertFloat():
    assert 3.1 == 3.1

def test_assertString():
    assert "3" == "3"

def test_assertArray():
    assert [1,2,3] == [1,2,3]

def test_assertDictionary():
    assert {'1': 1} == {'1': 1}



def raiseException():
    raise ValueError

def test_assertException():
    with pytest.raises(ValueError):
        raiseException()

