import argparse
import sys

import quizzer.server as server
import quizzer.loaders.assessment_loader as assessment_loader
import quizzer.loaders.tests_loader as tests_loader
import quizzer.serializers.assessment_serializer as assessment_serializer


__author__ = 'David Moreno García'


def calculate_grades(questions_url, answers_url):
    """
    Calculate assessments' grades given the urls to the questions and answers files.

    :param questions_url: URL to the questions file
    :param answers_url: URL to the answers file
    :return: a new assessment with containing questions, answers and calculated grades
    """
    assessment = assessment_loader.load_assessment_from_urls(questions_url, answers_url, None)
    assessment.calculate_grades()

    return assessment


def show_grades(grades, format):
    """
    Show the grades received as argument in the format specified.

    :param grades: grades to show
    :param format: format of the output
    """
    print('Assessment\'s grades')
    print(assessment_serializer.serialize_grades(grades, format) + "\n")


def show_statistics(statistics, format):
    """
    Show the statistics received as argument in the format specified.

    :param statistics: statistics to show
    :param format: format of the output
    """
    print('Assessment\'s statistics')
    print(assessment_serializer.serialize_statistics(statistics, format) + "\n")


def validate_assessments(url):
    """
    Validate tests inside of the file referenced by the URL argument.

    :param url: URL to the tests file
    """
    valid = True

    for test in tests_loader.load_all_tests(url):
        assessment = assessment_loader.load_assessment_from_urls(test.questions_url, test.answers_url, test.grades_url)

        if assessment.validate_grades():
            print('Test valid')
        else:
            valid = False
            print('Test not valid')

    print('All tests OK') if valid else print('Tests failed')


# Parse command line arguments and decide what method to call next
parser = argparse.ArgumentParser()
parser.add_argument('-a', help='URL to the answers file')
parser.add_argument('-o', help='Generate output in the specified format (json or xml)')
parser.add_argument('-q', help='URL to the questions file')
parser.add_argument('-s', help='Show questions statistics', action='store_true')
parser.add_argument('-t', help='Validate assessments in tests file')

args = parser.parse_args()

if not len(sys.argv) > 1:
    server.app.run()
elif args.t:
    validate_assessments(args.t)
elif args.a and args.q:
    assessment = calculate_grades(args.q, args.a)

    output_format = args.o if args.o else 'json'

    show_grades(assessment._grades, output_format)

    if args.s:
        show_statistics(assessment.get_statistics(), output_format)
else:
    parser.print_help()