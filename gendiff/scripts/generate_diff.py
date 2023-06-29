from gendiff.gendiff import generate_diff


def main():
    print(
        generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json'))


if __name__ == '__main__':
    main()
