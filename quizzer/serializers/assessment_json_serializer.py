import json

__author__ = 'David Moreno García'


def serialize_grades(grades):
    """
    Returns an string with the representation of the grades in JSON format.

    :param grades: grades to serialize
    :return: an string with the representation in the desired format.
    """
    scores = list()

    for student_id, grade in grades.items():
        scores.append({"studentId": student_id, "value": grade.grade})

    return json.dumps({"scores": scores}, indent=4)


def serialize_statistics(statistics):
    """
    Returns an string with the representation of the statistics in JSON format.

    :param statistics: statistics to serialize
    :return: an string with the representation in the desired format
    """
    items = list()

    for question_id, correct_answers in statistics.items():
        items.append({"questionId": question_id, "correctAnswers": correct_answers})

    return json.dumps({"items": items}, indent=4)