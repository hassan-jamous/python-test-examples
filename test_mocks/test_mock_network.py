
import requests
import pytest
from unittest.mock import MagicMock

def getUrl(url):
    return requests.get(url)

def test_getUrl(monkeypatch):
    mock_response = MagicMock(requests.Response)
    mock_response.text = "text"
    
    mock_get = MagicMock()
    mock_get.return_value = mock_response

    monkeypatch.setattr("requests.get", mock_get)
    result = getUrl("http://www.google.com")

    mock_get.assert_called_once_with("http://www.google.com")
    assert result.text == "text"

