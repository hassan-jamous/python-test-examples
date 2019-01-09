import pytest 

@pytest.fixture()
def setupAndTearDownWithYield():
    print('setup')
    yield
    print('tear down')

@pytest.fixture()
def setupAndTearDownWithAddFinalizer(request):
    print('setup')

    def teardown_first():
        print('teardown first')

    def teardown_second():
        print('teardown second')

    request.addfinalizer(teardown_first)
    request.addfinalizer(teardown_second)

def test_assertTrue(setupAndTearDownWithYield):
    assert True


def test_assertTrue2(setupAndTearDownWithAddFinalizer):
    assert True