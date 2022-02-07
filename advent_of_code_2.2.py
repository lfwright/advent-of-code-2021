#!/usr/bin/python3

import sys

# define map to convert instructions

direction_to_orientation_dict = {
    ## instruction : (Postition index, orientation)
    'forward': ('horizontal', 1),
    'up': ('aim', -1),
    'down': ('aim', 1)
}
    
submarine_position = {
    'horizontal': 0,
    'vertical': 0,
    'aim': 0
}


if __name__ == '__main__':

    instructions = (line.rstrip() for line in sys.stdin)
    directions_and_distances = (line.split() for line in instructions)
    
 
    for direction, distance in directions_and_distances:
        orientation = direction_to_orientation_dict[direction]
        distance = int(distance)

        submarine_position[orientation[0]] += orientation[1] * distance
        if direction == 'forward':
            submarine_position['vertical'] += submarine_position['aim'] * distance
        print(direction, distance, submarine_position)


    print(submarine_position)
    print(submarine_position['horizontal'] * submarine_position['vertical'])
    
