#!/usr/bin/python3

import sys
import itertools
import collections

sign = lambda x: 1 if x > 0 else -1

def create_axis_points(point1, point2):
    
    return [axis_point for axis_point in range(point1, point2 + sign(point2 - point1), sign(point2 - point1))]

def create_line_points(x1, y1, x2, y2):
    xline_points = create_axis_points(x1, x2)
    yline_points = create_axis_points(y1, y2)

    axis_difference_map = {
        len(xline_points): xline_points,
        len(yline_points): yline_points
    }

    fill_point = axis_difference_map[min(len(xline_points), len(yline_points))][-1] # final element of the shortest list

    return itertools.zip_longest(xline_points, yline_points, fillvalue = fill_point)
        
if __name__ == '__main__':

    # turn input into 4 element list of int [x1, y1, x2, y2]
    
    line_end_points = (line for line in sys.stdin)
    end_point_strings = (line.split(" -> ") for line in line_end_points)
    end_point_pairs = ([int(end_point) for end_point_string in end_point_string_list for end_point in end_point_string.split(",")] for end_point_string_list in end_point_strings)

    point_counts = collections.Counter()
    
    for end_points in end_point_pairs:
        if end_points[0] == end_points[2] or end_points[1] == end_points[3]:
            for line_points in create_line_points(*end_points):
                point_counts.update([str(line_points)])

    points_greater_than_2_count = 0
    for elem, cnt in point_counts.items():
        if cnt >= 2:
            points_greater_than_2_count += 1

    print(points_greater_than_2_count)
