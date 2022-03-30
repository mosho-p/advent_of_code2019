# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

# How many different passwords within the range given in your puzzle input meet these criteria?
# Your puzzle input is 265275-781584.

count = 0

for x in range(265276, 781584):
    s = str(x)
    if s != ''.join(sorted(s)):
        continue
    dupes = [str(s[i]==s[i+1]) for i in range(5)]
    if ['True', 'False'] == dupes[:2] or ['False', 'True'] == dupes[-2:] or 'FalseTrueFalse' in ''.join(dupes):
        count += 1

print(count)
