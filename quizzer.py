import argparse
import sys

import quizzer.loaders.assessment_loader as assessment_loader
import quizzer.loaders.tests_loader as tests_loader
import quizzer.serializers.assessment_serializer as assessment_serializer


__author__ = 'David Moreno García'


def calculate_grades(questions_url, answers_url):
    assessment = assessment_loader.load_assessment_from_urls(questions_url, answers_url, None)
    assessment.calculate_grades()

    return assessment


def show_grades(grades, format):
    print('Assessment\'s grades')
    print(assessment_serializer.serialize_grades(grades, format) + "\n")


def show_statistics(statistics, format):
    print('Assessment\'s statistics')
    print(assessment_serializer.serialize_statistics(statistics, format) + "\n")


def validate_assessments(url):
    valid = True

    for test in tests_loader.load_all_tests(url):
        assessment = assessment_loader.load_assessment_from_urls(test.questions_url, test.answers_url, test.grades_url)

        if assessment.validate_grades():
            print('Test valid')
        else:
            valid = False
            print('Test not valid')

    print('All tests OK') if valid else print('Tests failed')

parser = argparse.ArgumentParser()
parser.add_argument('-a', help='URL to the answers file')
parser.add_argument('-o', help='Generate output in the specified format (json or xml)')
parser.add_argument('-q', help='URL to the questions file')
parser.add_argument('-s', help='Show questions statistics', action='store_true')
parser.add_argument('-t', help='Validate assessments in tests file')

args = parser.parse_args()

if not len(sys.argv) > 1:
    print('No arguments')
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