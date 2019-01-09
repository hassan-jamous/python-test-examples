def setup_module(function):
    print('setup_module')

def teardown_module(function):
    print('teardown_module')

def test_assertTrue():
    assert True

def test_assertFalse():
    assert False == False