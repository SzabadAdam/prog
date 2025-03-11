# TODO
import sys

def count_of_odds(numbers: list[int]) -> int:
    ret = 0
    for n in numbers:
        ret += n%2
    return ret

def main():
    for line in sys.stdin:
        tokens = line.strip().split()
        numbers = []
        for n in tokens:
            numbers.append(int(n))
        print(count_of_odds(numbers))

if __name__ == "__main__":
    main()
