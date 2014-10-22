__author__ = 'David Moreno García'


def serialize_grades(grades):
    """
    Returns an string with the representation of the grades in XML format.

    :param grades: grades to serialize
    :return: an string with the representation in the desired format
    """
    result = '<scores>\n'

    for student_id, grade in grades.items():
        result += "\t<score>\n\t\t<studentId>" + str(student_id) + "</studentId>\n"
        result += "\t\t<value>" + str(grade.grade) + "</value>\n\t</score>\n"

    return result + '</scores>'


def serialize_statistics(statistics):
    """
    Returns an string with the representation of the statistics in XML format.

    :param statistics: statistics to serialize
    :return: an string with the representation in the desired format
    """
    result = '<statistics>\n'

    for question_id, correct_answers in statistics.items():
        result += "\t<item>\n\t\t<questionId>" + str(question_id) + "</questionId>\n"
        result += "\t\t<correctAnswers>" + str(correct_answers) + "</correctAnswers>\n\t</item>\n"

    return result + '</statistics>'