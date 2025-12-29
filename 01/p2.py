import sys

def cycle_counter(pointer: int, distance: int, range: int) -> int:
    cycles = 0
    new_pointer = pointer + distance 

    while(new_pointer < 0):
        new_pointer += 100
        cycles += 1

    while(new_pointer >= range):
        new_pointer -= 100
        cycles += 1

    return cycles

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
    
    counter += cycle_counter(dial_pointer, dir * dist, dial_range)
    dial_pointer = (dial_pointer + (dir * dist)) % dial_range
    
print(counter)
