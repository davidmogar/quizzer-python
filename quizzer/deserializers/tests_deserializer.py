import json
from quizzer.domain.test import Test

__author__ = 'David Moreno García'


class TestsDeserializer:
    @staticmethod
    def deserialize(json_string):
        tests = list()

        if json:
            data = json.loads(json_string)
            if 'tests' in data:
                for test in data['tests']:
                    if 'quizz' in test and 'assessment' in test and 'scores' in test:
                        tests.append(Test(test['quizz'], test['assessment'], test['scores']))

        return tests
