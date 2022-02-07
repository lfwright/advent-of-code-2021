#!/usr/bin/python3
import sys


def mean(observations):
    total = sum(observations)
    count = len(observations)

    print("total: ", total, " count: ", count)
    return total/count

def median(observations):
    size = len(observations)
    median_position = int(round(size/2))

    observations.sort()
    median_value = observations[median_position]

    return median_value

def sum_to_first_integer(n):
    return n*(n+1) / 2

def crab_cost_function(observations, alignment_position):
    return sum([sum_to_first_integer(abs(observation-alignment_position)) for observation in observations])

if __name__ == '__main__':

    crab_locations_io = (line for line in sys.stdin)
    crab_locations = [int(crab_location) for crab_location_str in crab_locations_io for crab_location in crab_location_str.split(",")]

    crab_locations.sort()
    
    try_next_position = True
    position_to_attempt = min(crab_locations)
    last_cost = crab_cost_function(crab_locations, position_to_attempt)
    
    while position_to_attempt != max(crab_locations):
        position_to_attempt += 1
       # print(position_to_attempt, last_cost)
        if last_cost <= crab_cost_function(crab_locations, position_to_attempt):
            print("final", position_to_attempt - 1, last_cost)
            break
        last_cost = crab_cost_function(crab_locations, position_to_attempt)
