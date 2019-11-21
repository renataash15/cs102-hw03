import sys
from statistics import mean

def main():
    assert len(sys.argv) > 1, "No input file path specified."

    input_file_path = sys.argv[1]
    print(f"Processing input file: {input_file_path}")


    a = open(input_file_path, "r")
    for line in a:
        x = line.split(',')
        numbers = []
        for n in x:
            numbers.append(float(n))
        avg = mean(numbers)
        print(avg)

if __name__ == "__main__":
    main()

