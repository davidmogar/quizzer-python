import os
from unittest import TestCase
import quizzer.deserializers.tests_deserializer as tests_deserializer

__author__ = 'David Moreno García'


class TestTestsDeserializer(TestCase):

    tests_url = 'tests/resources/tests.json'

    def test_deserialize(self):
        self.assertTrue(os.path.exists(self.tests_url), 'Missing tests file')

        tests = tests_deserializer.deserialize(open(self.tests_url, 'r').read())

        self.assertTrue(len(tests) == 1, 'Unexpected size for tests array')
        self.assertTrue(tests[0].questions_url == 'tests/resources/questions.json')
        self.assertTrue(tests[0].grades_url == 'tests/resources/grades.json')