import pytest

@pytest.fixture(scope="function", autouse=True)
def setup():
    print('fixture')

def test_assertTrue_withFixture_as_parameter():
    assert True

def test_assertFalse_withFixture_as_annotation():
    assert False == False