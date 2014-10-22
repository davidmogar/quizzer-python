import json

__author__ = 'David Moreno García'


def serialize_grades(grades):
    scores = list()

    for student_id, grade in grades.items():
        scores.append({"studentId": student_id, "value": grade.grade})

    return json.dumps({"scores": scores}, indent=4)


def serialize_statistics(statistics):
    items = list()

    for question_id, correct_answers in statistics.items():
        items.append({"questionId": question_id, "correctAnswers": correct_answers})

    return json.dumps({"items": items}, indent=4)