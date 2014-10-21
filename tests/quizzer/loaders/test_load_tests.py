import os
from unittest import TestCase
import quizzer.loaders.tests_loader as tests_loader

__author__ = 'David Moreno García'


class TestLoad_tests(TestCase):

    tests_url = 'tests/resources/tests.json'

    def test_load_tests(self):
        self.assertTrue(os.path.exists(self.tests_url), 'Missing tests file')

        try:
            tests = tests_loader.load_tests(self.tests_url)
            self.assertTrue(len(tests) == 1, 'Unexpected tests array size')
        except Exception:
            self.fail('Exception not expected')