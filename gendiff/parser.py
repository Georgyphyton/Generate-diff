import os
import json
import yaml


def pass_to_file(file):
    return os.path.join('tests', 'fixtures', file)


def parse(file):
    path = pass_to_file(file)
    form = os.path.splitext(path)[1][1:]
    with open(path) as f:
        if form == 'json':
            return json.load(f)
        elif form in ('yml', 'yaml'):
            return yaml.safe_load(f)
        else:
            raise ValueError(f"Unrecognized extension: {form}")
