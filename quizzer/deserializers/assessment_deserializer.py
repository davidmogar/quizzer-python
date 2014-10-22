import json
from quizzer.domain.answer import Answer
from quizzer.domain.grade import Grade
from quizzer.domain.questions import *

__author__ = 'David Moreno García'


def deserialize_answers(json_string):
    """
    Deserializes the JSON representation received as arguments to a map of student ids to Answer objects.

    :param json_string: JSON representation of the answers objects
    :return: a map of student ids to Answer objects
    """
    answers = dict()

    if json_string:
        data = json.loads(json_string)
        if 'items' in data:
            for item in data['items']:
                try:
                    answers[item['studentId']] = [Answer(answer['question'], answer['value']) for answer in
                                                  item['answers']]
                except KeyError:
                    pass

    return answers


def deserialize_grades(json_string):
    """
    Deserializes the JSON representation received as arguments to a map of student ids to Grade objects.

    :param json_string: JSON representation of the grades objects
    :return: a map of student ids to Grade objects
    """
    grades = dict()

    if json_string:
        data = json.loads(json_string)
        if 'scores' in data:
            for grade in data['scores']:
                if 'studentId' in grade and 'value' in grade:
                    grades[grade['studentId']] = Grade(grade['studentId'], grade['value'])

    return grades


def deserialize_multichoice(hash):
    """
    Deserialize a Multichoice question
    :param hash: HashMap containing the question data
    :return: question created
    """
    question = MultichoiceQuestion(hash['id'], hash['questionText'])

    if 'alternatives' in hash:
        for alternative in hash['alternatives']:
            if 'code' in alternative and 'text' in alternative and 'value' in alternative:
                question.add_alternative(alternative['code'], alternative['text'], alternative['value'])

    return question


def deserialize_numerical(hash):
    """
    Deserialize a Numerical question
    :param hash: HashMap containing the question data
    :return: question created
    """
    question = NumericalQuestion(hash['id'], hash['questionText'])

    if 'correct' in hash:
        question.correct = hash['correct']
    if 'valueOk' in hash:
        question.value_correct = hash['valueOk']
    if 'valueFailed' in hash:
        question.value_incorrect = hash['valueFailed']

    return question


def deserialize_true_false(hash):
    """
    Deserialize a True/False question
    :param hash: HashMap containing the question data
    :return: question created
    """
    question = TrueFalseQuestion(hash['id'], hash['questionText'])

    if 'correct' in hash:
        question.correct = hash['correct']
    if 'valueOK' in hash:
        question.value_correct = hash['valueOK']
    if 'valueFailed' in hash:
        question.value_incorrect = hash['valueFailed']
    if 'feedback' in hash:
        question.feedback = hash['feedback']

    return question

# Hash used to decide what method to call based on the question type
question_type = {
    'multichoice': deserialize_multichoice,
    'numerical': deserialize_numerical,
    'truefalse': deserialize_true_false
}


def deserialize_questions(json_string):
    """
    Deserializes the JSON representation received as arguments to a map of questions ids to Question objects.

    :param json_string: JSON representation of the questions objects
    :return: a map of questions ids to Question objects
    """
    questions = dict()

    if json_string:
        data = json.loads(json_string)
        if 'questions' in data:
            for question in data['questions']:
                try:
                    if 'id' in question and 'questionText' in question:
                        questions[question['id']] = question_type[question['type']](question)
                except KeyError:
                    pass

    return questions

