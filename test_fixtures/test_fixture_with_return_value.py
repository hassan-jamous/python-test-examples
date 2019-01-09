import pytest

@pytest.fixture()
def setup():
    print('setup')
    return 4

def test_assertTrue_withFixture_as_parameter(setup):
    print(setup)
    assert True
