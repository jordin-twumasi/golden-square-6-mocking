from lib.time_error import TimeError
from unittest.mock import Mock
import pytest

def test_calls_api_to_return_time_difference():
    requester_mock = Mock(name="requester")
    response_mock = Mock(name = "response")

    requester_mock.get.return_value = response_mock

    response_mock.json.return_value = {
       "unixtime" : 65
    }
    timer_mock = Mock()
    timer_mock.time.return_value = 64.9
    time_error = TimeError(requester_mock, timer_mock)
    assert time_error.error() == pytest.approx(0.1)