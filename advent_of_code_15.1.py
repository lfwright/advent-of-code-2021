#!/usr/bin/env python3

import numpy as np

class Error(Exception):
    pass

class DirectionArrayValueError(Error):
    pass

def load_data_into_array(data):
    risk_array = np.array(data)

    return risk_array

def find_previous_step_with_minimum_risk(risk_arr, cumulative_arr, direction_arr, index):
    i,j = index
    try:
        above_total_risk = cumulative_arr[max(i-1, 0), j]
        left_total_risk = cumulative_arr[i, max(j-1, 0)]
        if i == 0:
            cumulative_arr[index] = left_total_risk + risk_arr[index]
            direction_arr[index] = 1
        elif j == 0:
            cumulative_arr[index] = above_total_risk + risk_arr[index]
            direction_arr[index] = 2
        else:
            if left_total_risk < above_total_risk:
                cumulative_arr[index] = left_total_risk + risk_arr[index]
                direction_arr[index] = 1
            elif left_total_risk > above_total_risk:
                cumulative_arr[index] = above_total_risk + risk_arr[index]
                direction_arr[index] = 2
            else:
                cumulative_arr[index] = left_total_risk + risk_arr[index]
                direction_arr[index] = 1
                
    except(IndexError):
        pass

    return (cumulative_arr, direction_arr)
        
def mask_minimum_path(risk_array, direction_array):
    
    i,j = [i-1 for i in list(risk_array.shape)]
    
    highlighted_path_array = np.zeros_like(risk_array)
    highlighted_path_array[i,j] = risk_array[i,j]
    print(i,j)
    
    while (i,j) != (0,0):
        # 1 - leftward
        # 2 - upward
        try:
            if direction_array[i,j] == 1:
                i -= 1
            elif direction_array[i,j] == 2:
                j -= 1

            else:
                raise(DirectionArrayValueError)

            highlighted_path_array[i,j] = risk_array[i,j]
            print((i,j), direction_array[i,j])

        except(DirectionArrayValueError):
            print('Value Error raised walking path\n\narray entry: {}\nindex: {}'.format(direction_array[i,j], (i,j)))
            break
        
    return highlighted_path_array

def find_minimum_path(risk_array):
    temp_arrays = (np.zeros_like(risk_array), np.zeros_like(risk_array))

    for coord_total in range(max(risk_array.shape)*2):
        cells_to_compute = [(min(i, risk_array.shape[0]), min(coord_total-i, risk_array.shape[1])) for i in range(coord_total+1)]
        for cell_index in cells_to_compute:
            if cell_index == (0,0):
                continue
            temp_arrays = find_previous_step_with_minimum_risk(risk_array, temp_arrays[0], temp_arrays[1], cell_index)

    print(temp_arrays[0])
    print(temp_arrays[1])

    np.savetxt("./AOC15 cumulative array", temp_arrays[0], fmt="%.d", delimiter=" ")
    np.savetxt("./AOC15 direction array", temp_arrays[1], fmt="%.d", delimiter="")

    #walk the path back out
    minimum_risk_total = temp_arrays[0][-1, -1]
    return minimum_risk_total
    # highlighted_path_array = mask_minimum_path(risk_array, temp_arrays[1])
    

    # return (minimum_risk_total, highligthed_path_array)
 

if __name__ == "__main__":
    with open("./Advent Of Code data/AOC15", "r") as infile:
        data = [line.rstrip() for line in infile]
        
    risk_int_strips = [[int(char) for char in line] for line in data]
    risk_array = load_data_into_array(risk_int_strips)

#    minimum_risk, minimum_risk_path =
    print(find_minimum_path(risk_array))
 #   print("minimum risk: {}\nminimum risk path{}".format(minimum_risk, minimum_risk_path))

    

    
