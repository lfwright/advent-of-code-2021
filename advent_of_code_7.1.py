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

if __name__ == '__main__':

    crab_locations_io = (line for line in sys.stdin)
    crab_locations = [int(crab_location) for crab_location_str in crab_locations_io for crab_location in crab_location_str.split(",")]

    crab_distance_median = median(crab_locations)
    print(crab_distance_median)

    fuel_used_moving_crabs = sum([abs(crab_location - crab_distance_median) for crab_location in crab_locations])
    print(fuel_used_moving_crabs)
