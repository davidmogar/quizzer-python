__author__ = 'David Moreno García'


def serialize_grades(grades):
    result = '<scores>\n'

    for student_id, grade in grades.items():
        result += "\t<score>\n\t\t<studentId>" + str(student_id) + "</studentId>\n"
        result += "\t\t<value>" + str(grade.grade) + "</value>\n\t</score>\n"

    return result + '</scores>'


def serialize_statistics(statistics):
    result = '<statistics>\n'

    for question_id, correct_answers in statistics.items():
        result += "\t<item>\n\t\t<questionId>" + str(question_id) + "</questionId>\n"
        result += "\t\t<correctAnswers>" + str(correct_answers) + "</correctAnswers>\n\t</item>\n"

    return result + '</statistics>'