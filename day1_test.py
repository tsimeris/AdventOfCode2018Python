import day1

"""
    +1, +1, +1 results in  3
    +1, +1, -2 results in  0
    -1, -2, -3 results in -6
"""

part1_expectations = [
    ("+1 +1 +1", 3),
    ("+1 +1 -2", 0),
    ("-1 -2 -3", -6)
]

for (input, output) in part1_expectations:
    computed = day1.compute_frequency(input)
    assert computed == output, "(%s,%d) -> %d"%(input, output, computed)

"""
    On the input file, the answer should be correct
"""

part_1_answer = 592
assert day1.part_1() == part_1_answer

"""
    +1, -1 first reaches 0 twice.
    +3, +3, +4, -2, -4 first reaches 10 twice.
    -6, +3, +8, +5, -6 first reaches 5 twice.
    +7, +7, -2, -7, -4 first reaches 14 twice.
"""

part2_expectations = [
    ("+1 -1", 0),
    ("+3 +3 +4 -2 -4", 10),
    ("-6 +3 +8 +5 -6", 5),
    ("+7 +7 -2 -7 -4", 14)
]

for (input, output) in part2_expectations:
    computed = day1.find_duplicate(input)
    assert computed == output, "(%s,%d) -> %d"%(input, output, computed)

"""
    On the input file, the answer should be correct
"""

part_2_answer = 241
assert day1.part_2() == part_2_answer