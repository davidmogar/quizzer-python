import quizzer.deserializers.tests_deserializer as tests_deserializer
import quizzer.utils.url_reader as urlreader

__author__ = 'David Moreno García'


def load_all_tests(tests_url):
    if not tests_url:
        raise AttributeError("Tests URL cannot be null")

    json = urlreader.read(tests_url)

    return tests_deserializer.deserialize(json)