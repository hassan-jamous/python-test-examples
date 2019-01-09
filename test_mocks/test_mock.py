import os
import pytest
from unittest.mock import MagicMock

def readFromFile(filename):
    if not os.path.exists(filename):
        raise Exception("file doesnt exist")
    infile = open(filename, "r")
    line = infile.readline()
    return line

def test_mock_the_read(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock()
    mock_file.readline.return_value = "test line"

    mock_open = MagicMock()
    mock_open.return_value = mock_file
    monkeypatch.setattr("builtins.open", mock_open)

    mock_exist = MagicMock()
    mock_exist.return_value = True
    monkeypatch.setattr("os.path.exists", mock_exist)

    result = readFromFile("whatever")
    mock_open.assert_called_once_with("whatever", "r")

    assert result == "test line"


def test_mock_throwing_exception(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock()
    mock_file.readline.return_value = "test line"

    mock_open = MagicMock()
    mock_open.return_value = mock_file
    monkeypatch.setattr("builtins.open", mock_open)

    mock_exist = MagicMock()
    mock_exist.return_value = False
    monkeypatch.setattr("os.path.exists", mock_exist)

    with pytest.raises(Exception):
        readFromFile("doesnt exist")
