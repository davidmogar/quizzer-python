from unittest import TestCase

from quizzer.assessment import Assessment
from quizzer.domain.answer import Answer
from quizzer.domain.grade import Grade
from quizzer.domain.questions import *

__author__ = 'David Moreno García'


class TestAssessment(TestCase):
    def setUp(self):
        self._assessment = Assessment()

        questions = dict()
        answers = dict()

        multichoice = MultichoiceQuestion(1, 'Question 1')
        multichoice.add_alternative(1, 'Alternative 1', 0)
        multichoice.add_alternative(2, 'Alternative 2', 0.75)
        questions[1] = multichoice

        numerical = NumericalQuestion(2, 'Question 2')
        numerical.correct = 4.3
        numerical.value_correct = 1
        numerical.value_incorrect = -0.5
        questions[2] = numerical

        truefalse = TrueFalseQuestion(3, 'Question 3')
        truefalse.correct = True
        truefalse.value_correct = 1
        truefalse.value_incorrect = -0.25
        questions[3] = truefalse

        answers[1] = [Answer(1, 2), Answer(2, 4.3), Answer(3, True)]
        answers[2] = [Answer(1, 1), Answer(2, 2), Answer(3, False)]
        answers[3] = [Answer(1, 2), Answer(2, 2), Answer(3, True)]

        self._assessment._questions = questions
        self._assessment._answers = answers

    def test_calculate_grades(self):
        self._assessment.calculate_grades()

        self.assertTrue(len(self._assessment._grades) == 3, 'Unexpected grades size')
        self.assertAlmostEqual(self._assessment._grades[1].grade, 2.75, 'Unexpected grade value for id 1', 0.05)
        self.assertAlmostEqual(self._assessment._grades[2].grade, -0.75, 'Unexpected grade value for id 2', 0.05)

    def test_calculate_student_grade(self):
        self.assertAlmostEqual(self._assessment.calculate_student_grade(1), 2.75,
                               'Unexpected grade value for id 1', 0.05)
        self.assertAlmostEqual(self._assessment.calculate_student_grade(2), -0.75,
                               'Unexpected grade value for id 2', 0.05)

    def test_get_statistics(self):
        statistics = self._assessment.get_statistics()

        self.assertTrue(statistics[1] == 2, 'Unexpected value for question 1 statistics')
        self.assertTrue(statistics[2] == 1, 'Unexpected value for question 2 statistics')
        self.assertTrue(statistics[3] == 2, 'Unexpected value for question 3 statistics')

    def test_validate_grade(self):
        self.assertTrue(self._assessment.validate_grade(Grade(1, 2.75)), 'Unexpected grade validation result for id 1')
        self.assertTrue(self._assessment.validate_grade(Grade(2, -0.75)), 'Unexpected grade validation result for id 2')

    def test_validate_grades(self):
        grades = dict()
        grades[1] = Grade(1, 2.75)
        grades[2] = Grade(2, -0.75)

        self._assessment._grades = grades
        self.assertTrue(self._assessment.validate_grades(), 'Unexpected validation result. Expected a valid grade')

        grades = dict()
        grades[1] = Grade(1, 2.75)
        grades[2] = Grade(2, 0.25)

        self._assessment._grades = grades
        self.assertFalse(self._assessment.validate_grades(), 'Unexpected validation result. Expected a non valid grade')