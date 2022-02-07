#!/usr/bin/python3
import sys
import collections
from math import prod


def is_minimum_of_neighbours(centre, neighbours):
    return centre < min(neighbours)

def give_value_if_possible(index, iterable, fill):
    try:
        if index < 0:
            return fill
        else:
            return iterable[index]
    except IndexError:
        return fill
    
def test_heights(test_queue):
    low_points = []
    for queue_index, mid_point in enumerate(test_queue[1]):
        neighbours = [give_value_if_possible(queue_index + diff, queue_list, 10) for diff, queue_list in (
            (0, test_queue[0]),
            (-1, test_queue[1]),
            (1, test_queue[1]),
            (0, test_queue[2])
        )]
        if is_minimum_of_neighbours(mid_point, neighbours):
            low_points.append(mid_point)

    return low_points

def is_part_of_basin(centre, neighbours):
    neighbours = [neighbour for neighbour in neighbours if (neighbour is not None and neighbour != 0)]

    try:
        basin = min(neighbours)
    except ValueError:
        basin = 0

    return basin

def identify_basins(previous_deque, height_strip,id_counter):
    try:
        new_basin_id = max(max(id_counter), max(previous_deque[0]), max(previous_deque[1]))+1
    except ValueError:
        new_basin_id = 1

    new_previous_ids = []
    next_ids = []

    for height_index, mid_point in enumerate(height_strip):
        neighbours = [give_value_if_possible(height_index + diff, iterable, None) for diff, iterable in (
            (0, previous_deque[1]),
            (-1, next_ids)
        )]
        
        if mid_point == 9:
            next_ids.append(0)
            new_previous_ids.append(give_value_if_possible(height_index, previous_deque[1], 0))
            
        elif is_part_of_basin(mid_point, neighbours):
            try:
                basin = is_part_of_basin(mid_point, neighbours)

                #replace last element of next ids
                next_ids[-1] = min(next_ids[-1], basin)
                next_ids.append(basin)

                #replace element of new previous ids
                new_previous_ids.append(min(basin, give_value_if_possible(height_index, previous_deque[1], 0)))
              

            except IndexError:
                next_ids.append(basin)
                new_previous_ids.append(min(basin, give_value_if_possible(height_index, previous_deque[1], 0)))

        else:
            next_ids.append(new_basin_id)
            new_previous_ids.append(give_value_if_possible(height_index, previous_deque[1], 0))            
            new_basin_id += 1

    
    print("{}\t{}".format(next_ids, height_strip))
    return (new_previous_ids, next_ids)
            
if __name__ == '__main__':

    heightmap_IO = (line.rstrip() for line in sys.stdin)
    heightmap_points_lists = ([int(char) for i, char in enumerate(line) ] for line in heightmap_IO)

    basin_id_counts = collections.Counter()
    
    previous_ids = collections.deque(maxlen=2)
    previous_ids.append([0])
    previous_ids.append([0])

    for heightmap_points in heightmap_points_lists:
        
        new_previous_ids, next_ids = identify_basins(previous_ids, heightmap_points, basin_id_counts)
        
        previous_ids.pop()
        previous_ids.append(new_previous_ids)
        previous_ids.append(next_ids)
        basin_id_counts.update(previous_ids[0])
        print(previous_ids)

    basin_id_counts.update(previous_ids[1])
    del basin_id_counts[0]
    print(basin_id_counts.most_common(3))
    print(prod(basin_id_count[1] for basin_id_count in basin_id_counts.most_common(3)))
