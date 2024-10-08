"""
Below the message, the device shows a sequence of changes in frequency (your puzzle input). A value like +6 means the current frequency increases by 6; a value like -3 means the current frequency decreases by 3.

For example, if the device displays frequency changes of +1, -2, +3, +1, then starting from a frequency of zero, the following changes would occur:

    Current frequency  0, change of +1; resulting frequency  1.
    Current frequency  1, change of -2; resulting frequency -1.
    Current frequency -1, change of +3; resulting frequency  2.
    Current frequency  2, change of +1; resulting frequency  3.

In this example, the resulting frequency is 3.

Here are other example situations:

    +1, +1, +1 results in  3
    +1, +1, -2 results in  0
    -1, -2, -3 results in -6

Note that the input is not comma separated, but newline separated
"""

def parse_input(content):
    # split on newlines / other whitespace
    entries = content.split()
    result = []
    for entry in entries:
        result.append(int(entry))
    return result

def compute_frequency(input):
    parsed_input = parse_input(input)
    frequency = 0
    for change in parsed_input:
        frequency += change
    return frequency

def part_1():
    with open("day1.input", "r") as f:
        raw_input = f.read()
    return compute_frequency(raw_input)



"""
You notice that the device repeats the same frequency change list over and over.
To calibrate the device, you need to find the first frequency it reaches twice.
"""

def cycle_frequencies(input):
    while True:
        for element in input:
            yield element

def find_duplicate(raw_input):
    cycle = cycle_frequencies(parse_input(raw_input))
    seen = {}
    step = 0
    current = 0
    for change in cycle:
        if current in seen:
            return current
        seen[current] = step
        step += 1
        current += change

def part_2():
    with open("day1.input", "r") as f:
        raw_input = f.read()
    return find_duplicate(raw_input)



if __name__ == "__main__":
    print("part 1:", part_1())
    print("part 2:", part_2())