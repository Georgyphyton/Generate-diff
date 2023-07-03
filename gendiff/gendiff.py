import argparse
from gendiff.parser import parse
from gendiff.dict_gendiff import dict_diff
from gendiff.format.stylish import to_stylish
from gendiff.format import formater


def parsik():
    parser = argparse.ArgumentParser(
        description='Compares two configurat files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    return parser.parse_args()


def generate_diff(file1, file2, format=to_stylish):
    lines1 = parse(file1)
    lines2 = parse(file2)
    result = dict_diff(lines1, lines2)
    return formater(result, format)
