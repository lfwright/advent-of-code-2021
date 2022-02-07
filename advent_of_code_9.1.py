#!/usr/bin/python3
import sys
import collections



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

def is_part_of_basin(neighbours):
    replace_none_with_zero = lambda x : x or 0
    return max([replace_none_with_zero(neighbour) for neighbour in neighbours])

def identify_basins(previous_ids, height_strip,id_counter):

    new_basin_id = max(id_counter) +1
    return_ids = []

    for height_index, mid_point in enumerate(height_strip):
        neighbours = [give_value_if_possible(height_index + diff, iterable, None) for diff, iterable in (
            (0, previous_ids),
            (-1, next_ids)
        )]
        
        if is_part_of_basin(neighbours):
            next_ids.append(is_part_of_basin)
        else:
            next_ids.append(new_basin_id)
            new_basin_id += 1

    return next_ids
            
    
    #TODO: Check the before and above heights for an id, if an id is found assign that id to the current elem, else  assign a new id, else if 9 then assign nothing
    #TODO: return the list of ids

if __name__ == '__main__':

    heightmap_IO = (line.rstrip() for line in sys.stdin)
    heightmap_points_lists = ([int(char) for char in line] for line in heightmap_IO)

    basin_id_counts = collections.Counter()
    
    previous_ids = []

    for heightmap_points in heightmap_points_lists:
        previous_ids = identify_basins(previous_ids, heightmap_points, basin_id_counts)
        basin_id_counts.update(previous_ids)
    
    # TODO: use previous id list in the find next id function to id basins
    # TODO: add the id counts from the returned list to the counter

    print(basin_id_counts)
