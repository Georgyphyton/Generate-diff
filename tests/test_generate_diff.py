from gendiff.gendiff import generate_diff
from gendiff.parser import parse
import pytest


@pytest.mark.parametrize(
        'input1,input2,output,format',
        [
            pytest.param(
                    'file1_flat.json',
                    'file2_flat.json',
                    'result.txt',
                    'stylish',
                    id='json flat'
                    ),
            pytest.param(
                    'file1_flat.yaml',
                    'file2_flat.yaml',
                    'result.txt',
                    'stylish',
                    id='yaml flat'),
            pytest.param(
                    'file1_dict.json',
                    'file2_dict.json',
                    'result_dict.txt',
                    'stylish',
                    id='json dict'),
            pytest.param(
                    'empty_file.json',
                    'empty_file.json',
                    'empty_result.txt',
                    'stylish',
                    id='empty file'),
            pytest.param(
                    'file1_dict.yaml',
                    'file2_dict.yaml',
                    'result_dict.txt',
                    'stylish',
                    id='yaml dict'),
            pytest.param(
                    'file1_dict.json',
                    'file2_dict.json',
                    'result_plain_dict.txt',
                    'plain',
                    id='empty file')])
def test_json(input1, input2, output, format):
    assert generate_diff(input1, input2, format) == parse(output)
