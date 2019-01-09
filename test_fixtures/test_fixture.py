import pytest

@pytest.fixture()
def setup():
    print('fixture')

def test_assertTrue_withFixture_as_parameter(setup):
    assert True

@pytest.mark.usefixtures("setup")
def test_assertFalse_withFixture_as_annotation():
    assert False == False