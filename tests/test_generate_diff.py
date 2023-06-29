from gendiff.gendiff import generate_diff
from tests import pass_to_file
import pytest


@pytest.mark.parametrize('input1,input2,output',
                         [pytest.param(
                            'file1.json', 'file2.json', 'test_json.txt',)])
def test_json(input1, input2, output):
    with open(pass_to_file(output)) as result:
        text_result = result.read()
        path1 = pass_to_file(input1)
        path2 = pass_to_file(input2)
        assert generate_diff(path1, path2) == text_result
