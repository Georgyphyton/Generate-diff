from gendiff.gendiff import generate_diff


def main():
    print(
        generate_diff('file1_flat.yaml', 'file2_flat.yaml'))


if __name__ == '__main__':
    main()
