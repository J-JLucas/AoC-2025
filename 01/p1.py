import sys

dial_pointer = 50;
dial_range = 100;
counter = 0;

for line in sys.stdin:
    line = line.rstrip("\n")
    dir = line[0]
    dist = int(line[1:])

    if dir == 'L':
        dir = -1
    else:
        dir = 1

    dial_pointer = (dial_pointer + (dir * dist)) % dial_range
    
    if dial_pointer == 0:
        counter += 1

print(counter)
