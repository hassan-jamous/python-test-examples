from abc import ABC, abstractmethod
from unittest.mock import MagicMock

class AbstractAdd(ABC):
    @abstractmethod
    def add(self, value1, value2):
        pass

class AddImplementation(AbstractAdd): 
    def add(self, value1, value2):
        return value1 + value2

def mainFunction(AbstractAdd):
    return AbstractAdd.add(1,2)


def test_abstract():
    mock_adder = MagicMock(AbstractAdd)
    mock_adder.add = MagicMock()
    mock_adder.add.return_value = 3

    result = mainFunction(mock_adder)
    mock_adder.add.assert_called_once_with(1,2)
    assert result == 3