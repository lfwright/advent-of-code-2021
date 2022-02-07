#!/usr/bin/env python3

import sys
import collections

def moving_sum_n_window(generator, n):
    last_n_elements = collections.deque(maxlen = n)
    
    for index, element in enumerate(generator):
        last_n_elements.append(int(element))
        if index >= n:
            yield sum(last_n_elements)

    
if __name__ == '__main__':

    depth_measurements = (line.rstrip() for line in sys.stdin)

    sum_3_depths = moving_sum_n_window(depth_measurements, 3)

    increases = 0
    last_depth = None
    for current_depth in sum_3_depths:
        if last_depth is not None:
            if last_depth < current_depth:
                increases += 1
        last_depth = current_depth
        print(current_depth, increases)

        
    print(increases)
