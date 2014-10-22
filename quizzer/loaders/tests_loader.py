import quizzer.deserializers.tests_deserializer as tests_deserializer
import quizzer.utils.url_reader as urlreader

__author__ = 'David Moreno García'


def load_all_tests(tests_url):
    """
    Returns a list of tests objects loaded from the file referenced by the URL argument.

    :param tests_url: URL to the tests file
    :return: a list of tests objects
    :exception: if there is an error while fetching content from the given URL
    """
    if not tests_url:
        raise AttributeError("Tests URL cannot be null")

    json = urlreader.read(tests_url)

    return tests_deserializer.deserialize(json)