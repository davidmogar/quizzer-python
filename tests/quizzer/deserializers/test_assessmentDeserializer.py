from unittest import TestCase

import quizzer.deserializers.assessment_deserializer as AssessmentDeserializer
from quizzer.domain.questions import *


__author__ = 'David Moreno García'


class TestAssessmentDeserializer(TestCase):
    questions_json = '''
        { "questions":
            [ { "type": "multichoice",
                "id" : 1,
                "questionText": "Scala fue creado por...",
                "alternatives": [
                    { "text": "Martin Odersky",   "code": 1, "value": 1 },
                    { "text": "James Gosling",    "code": 2, "value": -0.25 },
                    { "text": "Guido van Rossum", "code": 3, "value": -0.25 }
                ]
            },
            { "type" : "truefalse",
                "id" : 2,
                "questionText": "El creador de Ruby es Yukihiro Matsumoto",
                "correct": true,
                "valueOK": 1,
                "valueFailed": -0.25,
                "feedback": "Yukihiro Matsumoto es el principal desarrollador de Ruby desde 1996"
                }
            ]
        }
    '''
    answers_json = '''
        { "items":
         [ { "studentId": 234 ,
            "answers":
            [ { "question" : 1, "value": 1 },
              { "question" : 2, "value": false }
            ]
          },
          { "studentId": 245 ,
            "answers":
            [ { "question" : 1, "value": 1 },
              { "question" : 2, "value": true }
            ]
          },
          { "studentId": 221 ,
            "answers":
            [ { "question" : 1, "value": 2 } ]
          }
         ]
        }
    '''
    grades_json = '''
        { "scores":
         [ { "studentId": 234, "value": 0.75 } ,
           { "studentId": 245, "value": 2.0 } ,
           { "studentId": 221, "value": 0.75 }
         ]
        }
    '''

    def test_deserialize_answers(self):
        answers = AssessmentDeserializer.deserialize_answers(self.answers_json)

        self.assertIsNotNone(answers, 'Answers is none')
        self.assertTrue(len(answers) == 3, 'Unexpected size for answers map')
        self.assertTrue(len(answers[234]) == 2, 'Unexpected size for answers of student id 234')
        self.assertTrue(len(answers[245]) == 2, 'Unexpected size for answers of student id 245')
        self.assertTrue(len(answers[221]) == 1, 'Unexpected size for answers of student id 221')

    def test_deserialize_grades(self):
        grades = AssessmentDeserializer.deserialize_grades(self.grades_json)

        self.assertIsNotNone(grades, 'Grades is none')
        self.assertTrue(len(grades) == 3, 'Unexpected size for grades map')
        self.assertAlmostEqual(grades[234].grade, 0.75, 'Grade value for id', 0.05)
        self.assertAlmostEqual(grades[245].grade, 2, 'Grade value for id', 0.05)
        self.assertAlmostEqual(grades[221].grade, 0.75, 'Grade value for id', 0.05)

    def test_deserialize_questions(self):
        questions = AssessmentDeserializer.deserialize_questions(self.questions_json)

        self.assertIsNotNone(questions, 'Questions is none')
        self.assertTrue(len(questions) == 2, 'Unexpected size for questions map')
        self.assertTrue(isinstance(questions[1], MultichoiceQuestion), 'Unexpected type for question 1')
        self.assertTrue(isinstance(questions[2], TrueFalseQuestion), 'Unexpected type for question 2')
        self.assertTrue(questions[2].correct, 'Unexpected value for question 2')

        answers = AssessmentDeserializer.deserialize_answers(self.answers_json)
        self.assertAlmostEqual(questions[1].get_score(answers[234][0]), 1,
                               'Unexpected score for answer 1 of student 234', 0.05)