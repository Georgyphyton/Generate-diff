from gendiff.gendiff import parsik
from gendiff.gendiff import generate_diff


def main():
    args = parsik()
    print(
        generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
