import argparse


def random_names(path, number):
    raise raise NotImplementedError


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Returns a number of randomly picked names from the names.txt file')
    parser.add_argument('path', metavar='path', type=str, help='Path of the file with the list of names')
    parser.add_argument('--number', '-n', metavar='number', type=int, default=3, help='Number of names to ramdomly pick and return')
    args = parser.parse_args()
    names = random_names(args.path, args.number)
    print(*names, sep='\n')
