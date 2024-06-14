from math import sqrt

EPSILON = 1e-100

def sequence():
    current_count = sqrt(2)

    while True:

        previous_count = current_count
        current_count = sqrt(current_count + 2)

        if abs(previous_count - current_count) < EPSILON:
            return current_count

print(sequence())
