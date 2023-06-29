import argparse
import json
from tests import pass_to_file


def parsik():
    parser = argparse.ArgumentParser(
        description='Compares two configurat files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    return parser.parse_args()


def generate_diff(file1, file2):
    path1 = pass_to_file(file1)
    path2 = pass_to_file(file2)
    lines1 = json.load(open(path1))
    lines2 = json.load(open(path2))
    keys = lines1.keys() | lines2.keys()
    result = ['{']
    for key in sorted(keys):
        if key not in lines1:
            result.append(f'  + {key}: {str(lines2[key]).lower()}')
        elif key not in lines2:
            result.append(f'  - {key}: {str(lines1[key]).lower()}')
        elif lines1[key] == lines2[key]:
            result.append(f'  - {key}: {str(lines1[key]).lower()}')
            result.append(f'  + {key}: {str(lines2[key]).lower()}')
        else:
            result.append(f'    {key}: {str(lines1[key]).lower()}')
    return '\n'.join(result) + '\n}'
