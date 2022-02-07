#!/usr/bin/env python3
import numpy as np

DEBUG = {}

def debug_print(print_string, group):
    if group in DEBUG:
        print(print_string)

def load_points_into_array(points):
    x_max = max([point[0] for point in points])+1
    y_max = max([point[1] for point in points])+1

    point_array = np.zeros((x_max, y_max), dtype = np.int8)
    for i, j in points:
        
        point_array[i, j] = 1

    return point_array

def interpret_fold_instructions(fold_instructions):
    axis_map = {'x':0, 'y':1}
    return [(axis_map[fold[11]], int(fold[13:])) for fold in fold_instructions]

def perform_folds_on_array(points_array, fold_instructions):

    machine_fold_instructions = interpret_fold_instructions(fold_instructions)
    
    for instruction in machine_fold_instructions:
        fold_array_shape = list(points_array.shape)
        fold_array_shape[instruction[0]] -= instruction[1] # remainder of the array
        fold_array_shape = tuple(fold_array_shape)

        debug_print("----------", 2)
        debug_print(instruction[:], 2)
        debug_print(points_array.shape, 2)
        debug_print(fold_array_shape, 2)
        debug_print("----------", 2)

        debug_print(points_array, 1)

        debug_print("-----------------", 1)
        

        for index in np.ndindex(fold_array_shape):
            shifted_index = list(index)
            shifted_index[instruction[0]] += instruction[1]
            shifted_index = tuple(shifted_index)

            array_index = list(index)
            array_index[instruction[0]] = instruction[1] - index[instruction[0]]
            array_index = tuple(array_index)

            
            points_array[array_index] = max(points_array[shifted_index], points_array[array_index])
            points_array[shifted_index] = 0

    return points_array

def count_ones_in_array(points_array):
    visible_points_counter = 0
    for i, j in np.ndindex(points_array.shape):
        visible_points_counter += points_array[i, j]

    return visible_points_counter

if __name__ == "__main__":
    with open("./Advent Of Code data/AOC13", "r") as infile:
        data = [line.rstrip() for line in infile]

    points_data = [line for line in data if line[0:4] != "fold"]
    points_data.pop()    
    points_data = [[int(point) for point in line.split(",")] for line in points_data]
    
    instructions_data = [line for line in data if line[0:4] == "fold"]
    
    thermal_array = load_points_into_array(points_data)
    thermal_array = perform_folds_on_array(thermal_array, instructions_data)

    interpreted_folds = interpret_fold_instructions(instructions_data)
    i_folds = [fold[1] for fold in interpreted_folds if fold[0] == 1]
    j_folds = [fold[1] for fold in interpreted_folds if fold[0] == 0]
    
    thermal_array_to_print = thermal_array[:max(i_folds), :6]
   

    np.savetxt(fname="./AOC13 answer", X=thermal_array_to_print, fmt='%.d', delimiter="")
    
