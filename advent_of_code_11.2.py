#!/user/bin/env python3
import numpy as np

NUM_OF_ROUNDS = 400
FLASH_SHAPE = (
    (-1,-1),
    (0,-1),
    (1,-1),
    (-1,0),
    (1,0),
    (-1,1),
    (0,1),
    (1,1)
) 

def do_octopus_flashes(octo_array):
    are_flashes_remaining = 1
    i_max = octo_array.shape[0]
    j_max = octo_array.shape[1]
    new_flashes = 0
    
    while are_flashes_remaining:
        are_flashes_remaining = 0

        for i, j in np.ndindex(octo_array.shape):
            if octo_array[i, j] > 9:
                are_flashes_remaining = 1
                new_flashes += 1
                octo_array[i, j] = 0
                
                for f_i, f_j in FLASH_SHAPE:
                    if -1 < f_i+i < i_max and -1 < f_j+j < j_max and octo_array[f_i+i, f_j+j] != 0:
                        octo_array[f_i+i, f_j+j] += 1

    return octo_array, new_flashes

if __name__ == "__main__":

    with open("./Advent Of Code data/AOC11","r") as infile:
        data = [[int(num) for num in line.rstrip()] for line in infile.readlines()]

    
    octopus_array = np.array(data)
    octopus_round_energy_gain_array = np.ones_like(octopus_array)

    flash_total = 0
    run_next_step = 1
    round_num = 0
    
    while run_next_step:
        # test if all the elements are zero
        if not octopus_array.any():
            print("flashes synchronised: ", round_num)
            run_next_step = 0
            
        octopus_array = octopus_array+octopus_round_energy_gain_array
        octopus_array, new_flashes = do_octopus_flashes(octopus_array)
        round_num += 1
        #flash_total += new_flashes
    #print("the number of flashes is:", flash_total)
