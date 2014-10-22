import quizzer.serializers.assessment_json_serializer as json_serializer
import quizzer.serializers.assessment_xml_serializer as xml_serializer

__author__ = 'David Moreno García'


def serialize_grades(grades, format):
    """
    Returns an string with the representation of the grades in the desired format.

    :param grades: grades to serialize
    :param format: format of the output
    :return: an string with the representation in the desired format
    """
    if format == 'xml':
        result = xml_serializer.serialize_grades(grades)
    else:
        result = json_serializer.serialize_grades(grades)

    return result


def serialize_statistics(statistics, format):
    """
    Returns an string with the representation of the statistics in the desired format.

    :param statistics: statistics to serialize
    :param format: format of the output
    :return: an string with the representation in the desired format
    """
    if format == 'xml':
        result = xml_serializer.serialize_statistics(statistics)
    else:
        result = json_serializer.serialize_statistics(statistics)

    return result