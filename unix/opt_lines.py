import sys

def output_first_n_lines(f_name, n):
    with open(f_name, 'r') as file:
        lines = file.readlines()[:n]
        for line in lines:
            print(line.strip())

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <filename> <N>")
        sys.exit(1)

    f_name = sys.argv[1]
    n = int(sys.argv[2])
    output_first_n_lines(f_name, n)