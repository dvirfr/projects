import os
import argparse
import re


class Colour:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def finds_string_in_files(files_path, line_search):
    result_dict = {}
    s = line_search[0].upper() + '|' + line_search[0].lower()
    regex_word = '(.*)(%s)%s(.*)' % (s, line_search[1:])
    for r, d, f in os.walk(files_path):
        for file in f:
            os.chdir(files_path)
            with open(file) as search:
                for line_num, line in enumerate(search, 1):
                    line = line.rstrip()
                    if re.match(regex_word, line):
                        result_dict[line_num] = line
    return result_dict


def find_and_color(files_path, line_search):
    return_dict = finds_string_in_files(files_path, line_search)
    for key, value in return_dict.items():
        line_search = line_search.lower()
        if line_search in value:
            if line_search in value.lower():
                change = Colour.RED + line_search + Colour.END
                replace = value.replace(line_search, change)
                return_dict[key] = replace
                print("Found a match on line %s: %s" % (key, replace))

    return print("")


def find_and_underline():
    return_dict = finds_string_in_files(files_path, line_search)
    for key, value in return_dict.items():
        line_search = line_search.lower()
        if line_search in value:
            if line_search in value.lower():
                change = Colour.UNDERLINE + line_search + Colour.END
                replace = value.replace(line_search, change)
                return_dict[key] = replace
                print("Found a match on line %s: %s" % (key, replace))

    return print("")


parser = argparse.ArgumentParser()
parser.add_argument("-r", "--regex", required=True, type=str,
                    help="Write the word or strings you want to search for ")
parser.add_argument("-f", "--files", required=True, type=str,
                    help="Insert the path to the folder you want to search in")
parser.add_argument("-c", "--color", action="store_true",
                    help="chose this option to highlight the word you are looking for")
parser.add_argument("-u", "--underline", action="store_true",
                    help="chose this option to put underline under the matching words")

args = parser.parse_args()
under = args.underline
line_search = args.regex
files_path = args.files
color_result = args.color

if color_result:
    print(find_and_color(files_path, line_search))
elif under:
    print(find_and_underline(files_path, line_search))
else:
    run = finds_string_in_files(files_path, line_search)
    for k, v in run.items():
        print("Found a match on line %s: %s" % (k, v))
