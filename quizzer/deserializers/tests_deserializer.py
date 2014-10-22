import json
from quizzer.domain.test import Test

__author__ = 'David Moreno García'


def deserialize(json_string):
    """
    Deserializes the JSON representation received as arguments to a list of Test objects.

    :param json_string: JSON representation of Test objects
    :return: a list containing the tests deserialized
    """
    tests = list()

    if json_string:
        data = json.loads(json_string)
        if 'tests' in data:
            for test in data['tests']:
                if 'quizz' in test and 'assessment' in test and 'scores' in test:
                    tests.append(Test(test['quizz'], test['assessment'], test['scores']))

    return tests
