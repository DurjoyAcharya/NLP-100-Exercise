import sys

def output_last_n_lines(filename, n):
    with open(filename, 'r') as file:
        lines = file.readlines()[-n:]
        for line in lines:
            print(line.strip())

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Use: python opt_lines.py popular-names <Number of lines>")
        sys.exit(1)

    filename = sys.argv[1]
    n = int(sys.argv[2])
    output_last_n_lines(filename, n)
