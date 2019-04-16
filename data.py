import sys

def process(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    lines = lines[2:]
    lines = [line_to_points(line) for line in lines]
    x = [line[0] for line in lines]
    y = [line[1] for line in lines]
    return (x,y)

def line_to_points(line):
    line = line.rstrip('\n')
    line = line.split()
    return line

if __name__ == '__main__':
    data = process(sys.argv[1])
    print(data)