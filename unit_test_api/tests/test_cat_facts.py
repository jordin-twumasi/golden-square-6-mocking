from lib.cat_facts import CatFacts
from unittest.mock import Mock

def test_calls_api_to_return_fact():
    requester_mock = Mock()
    response_mock = Mock()

    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {
        "fact":"Smuggling a cat out of ancient Egypt was punishable by death. Phoenician traders eventually succeeded in smuggling felines, which they sold to rich people in Athens and other important cities.",
        "length":192
    }

    cat_fact = CatFacts(requester_mock)
    assert cat_fact.provide() == "Cat fact: Smuggling a cat out of ancient Egypt was punishable by death. Phoenician traders eventually succeeded in smuggling felines, which they sold to rich people in Athens and other important cities."