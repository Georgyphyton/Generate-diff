from gendiff.gendiff import generate_diff
from gendiff.parser import parse
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
                    id='yaml flat'),
            pytest.param(
                    'file1_dict.json',
                    'file2_dict.json',
                    'result_dict.txt',
                    id='json dict'),
            pytest.param(
                    'empty_file.json',
                    'empty_file.json',
                    'empty_result.txt',
                    id='empty file'),
            pytest.param(
                    'file1_dict.yaml',
                    'file2_dict.yaml',
                    'result_dict.txt',
                    id='yaml dict')])
def test_json(input1, input2, output):
    assert generate_diff(input1, input2) == parse(output)
