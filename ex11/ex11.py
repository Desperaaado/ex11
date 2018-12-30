import argparse
import sys

def parser_args():
    args = argparse.ArgumentParser(
        description='Realize sth like "uniq" command.'
    )
    args.add_argument(
        'file',
        help='file name',
        nargs='?'
    )
    return args.parse_args()

def get_lines(file):
    
    if not file:
        lines = sys.stdin.readlines()
    else:
        lines = open(file).readlines()

    return lines
    
def uniq_lines(lines):
    u_lines = []
    
    for line in lines:
        line = line.strip()
        if not (line in u_lines):
            u_lines.append(line)
            print(line)

    return u_lines

def become_uniq():
    args = parser_args()
    lines = get_lines(args.file)
    uniq_lines(lines)

become_uniq()