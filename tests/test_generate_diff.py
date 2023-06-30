from gendiff.gendiff import generate_diff
from gendiff.parser import pass_to_file
import pytest


@pytest.mark.parametrize(
        'input1,input2,output',
        [
            pytest.param(
                    'file1_flat.json',
                    'file2_flat.json',
                    'result.txt',
                    id='json flat'
                    ),
            pytest.param(
                    'file1_flat.yaml',
                    'file2_flat.yaml',
                    'result.txt',
                    id='yaml flat')])
def test_json(input1, input2, output):
    with open(pass_to_file(output)) as result:
        text_result = result.read()
        assert generate_diff(input1, input2) == text_result
