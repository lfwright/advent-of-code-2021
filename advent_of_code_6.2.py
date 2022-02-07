#!/usr/bin/python3
import collections
import sys

def move_forward_one_day(counter, breeding_resets):
    day_older_counter = collections.Counter({k-1:v for k,v in counter.items()})

    for days_till_breed in breeding_resets:
        day_older_counter[days_till_breed] += day_older_counter[-1]

    del day_older_counter[-1]
    return day_older_counter

def total_counter(counter):
    total = 0
    
    for k,v in counter.items():
        total += v

    return total
        
if __name__ == '__main__':

    MATURITY_DELAY = 2
    BREEDING_RESETS = (6,8)
    DAYS_TO_GO_FORWARD = 256
    

    laternfish_string = (line for line in sys.stdin)
    initial_laternfishs = [int(laternfish) for laternfish_str in laternfish_string for laternfish in laternfish_str.split(",")]

    laternfish_counter = collections.Counter(initial_laternfishs)

    for i in range(DAYS_TO_GO_FORWARD):
        laternfish_counter = move_forward_one_day(laternfish_counter, BREEDING_RESETS)

    print(laternfish_counter)
    print(total_counter(laternfish_counter))
    
