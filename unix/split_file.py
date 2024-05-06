import sys
import os

def split_file(filename, n):
    with open(filename, 'r') as file:
        lines = file.readlines()

    total_lines = len(lines)

    lines_per_piece = total_lines // n
    remainder = total_lines % n

    start = 0
    for i in range(n):
        piece_lines = lines_per_piece + (1 if i < remainder else 0)
        end = start + piece_lines
        with open(f"{filename}_part{i+1}", 'w') as outfile:
            outfile.writelines(lines[start:end])
        start = end

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Use: python split_file.py popular-names <Number of lines>")
        sys.exit(1)

    filename = sys.argv[1]
    n = int(sys.argv[2])

    split_file(filename, n)
