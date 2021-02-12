import argparse
import random


def is_valid_name(name):
    if name and not name.isdigit():
        return True
    return False

def get_file_lines(path):
    lines = []
    with open(path, 'r') as file_stream:
        lines = list(line.strip() for line in file_stream.read().splitlines() if line.strip())
    return lines

def random_names(path, number):
    names = []
    lines = get_file_lines(path)
    lines_processed = set()
    selected_names = list()

    # Loop until we have the desired number of names or there is no enough data
    while len(lines_processed) < len(lines) and len(selected_names) < number:
        line_number = random.randint(0, len(lines)-1)
        
        # Make sure the random line number has not been processed before
        if line_number not in lines_processed:
            lines_processed.add(line_number)

            # Validate the name and also keep track of its occurences to sort by
            name, occurences = lines[line_number].split(' ')
            name_already_exists = any(filter(lambda x: name == x[0], selected_names))
            if is_valid_name(name) and not name_already_exists:
                selected_names.append((name, occurences,))

    if len(selected_names) < number:
        raise ValueError("Not enough names in the list")

    # Return a descending ordered list of names
    return [item[0] for item in sorted(selected_names, key=lambda x: x[1], reverse=True)]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Returns a number of randomly picked names from the names.txt file')
    parser.add_argument('path', metavar='path', type=str, help='Path of the file with the list of names')
    parser.add_argument('--number', '-n', metavar='number', type=int, default=3, help='Number of names to ramdomly pick and return')
    args = parser.parse_args()
    names = random_names(args.path, args.number)
    print(*names, sep='\n')
