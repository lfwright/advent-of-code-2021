#!/usr/bin/python3

import sys
import collections


# define map to convert instructions

direction_to_orientation_dict = {
    ## instruction : (Postition index, orientation)
    'forward': ('horizontal', 1),
    'up': ('vertical', -1),
    'down': ('vertical', 1)
    }
    

if __name__ == '__main__':

    instructions = (line.rstrip() for line in sys.stdin)
    directions_and_distances = (line.split() for line in instructions)
    
    submarine_position = {
        'horizontal': 0,
        'vertical': 0
        }

    for direction, distance in directions_and_distances:
        orientation = direction_to_orientation_dict[direction]

        submarine_position[orientation[0]] += orientation[1] * int(distance)
        
    print(submarine_position)
    print(submarine_position['horizontal'] * submarine_position['vertical'])
    
