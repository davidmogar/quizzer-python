import os
import quizzer.loaders.assessment_loader as assessment_loader
from unittest import TestCase

__author__ = 'David Moreno García'


class TestAssessmentsLoader(TestCase):

    questions_url = 'tests/resources/questions.json'
    answers_url = 'tests/resources/answers.json'
    grades_url = 'tests/resources/grades.json'

    def test_load_assessment_from_urls(self):
        self.assertTrue(os.path.exists(self.questions_url), 'Missing questions file')
        self.assertTrue(os.path.exists(self.answers_url), 'Missing answers file')
        self.assertTrue(os.path.exists(self.grades_url), 'Missing grades file')

        try:
            assessment_loader.load_assessment_from_urls(self.questions_url, self.answers_url, self.grades_url)
            assessment_loader.load_assessment_from_urls(self.questions_url, self.answers_url, None)
        except Exception:
            self.fail('Exception not expected')