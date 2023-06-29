from gendiff.gendiff import generate_diff
from tests import pass_to_file


def test_json(file1, file2, result_file):
    with open(pass_to_file(result_file)) as result:
        text_result = result.read()
        assert generate_diff(file1, file2) == text_result
