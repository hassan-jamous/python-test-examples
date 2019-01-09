import pytest

@pytest.fixture(params=[1,2,3])
def setup(request):
    return request.param

def test_assertTrue_withFixture_as_parameter(setup):
    print(setup)
    assert True