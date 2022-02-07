#!/usr/bin/python3

## Do as before but recursively



import sys

def extract_bit(binary_to_check, n):
    mask = 1 << n # create binary string with 1 in nth position
    extract_bit = int(binary_to_check,2) & mask # extract the nth position from the input string
    return extract_bit >> n # return 0 or 1

def state_recursion_level(level):
    print(" " * level, "starting level ", level, " of recursion") 

def count_and_split_strings(binary_strings_list, bit_position, bit_criteria):
    """"
    take a list of binary strings, apply the logic and return a list of passing strings
    """
    
    # test if there is a singular string
    if len(binary_strings_list) == 1:
        print("final strings for ", bit_criteria, "is ", binary_strings_list)
        pass
    
    bit_position_count = 0

    binary_strings_0_split = []
    binary_strings_1_split = []
    
    binary_strings_splits_dict = {
        0: binary_strings_0_split,
        1: binary_strings_1_split
        }
    
    
    for binary_string in binary_strings_list:
        extracted_bit = extract_bit(binary_string, bit_position)

        bit_position_count += extracted_bit
        working_list = binary_strings_splits_dict[extracted_bit]
        working_list.append(binary_string)
        binary_strings_splits_dict[extracted_bit] = working_list

    #1 most common
    if bit_position_count + 0.5 > (len(binary_strings_list)/2): # draw decided by the bit_criteria
        most_common_strings = binary_strings_splits_dict[1]
        least_common_strings = binary_strings_splits_dict[0]

    #0 most common
    else:
        most_common_strings = binary_strings_splits_dict[0]
        least_common_strings = binary_strings_splits_dict[1]

    return (most_common_strings, least_common_strings)


    
def recursion_with_branch(func, high_branch_data, low_branch_data, criteria, level):    

    state_recursion_level(level + 1)

    data_of_interest  = high_branch_data if criteria else low_branch_data
    
    if level == -1 or len(data_of_interest) == 1:
        print("final level of recursion, Final data, ", (high_branch_data, low_branch_data))
        print(data_of_interest, int(data_of_interest[0], 2))
        return int(data_of_interest[0], 2)
    
    if criteria:
        high_branch_data, low_branch_data = func(high_branch_data, level, criteria)
    else:
        high_branch_data, low_branch_data = func(low_branch_data, level, criteria)

    return recursion_with_branch(func, high_branch_data, low_branch_data, criteria, level -1)

if __name__ == '__main__':

    binary_strings = (line.rstrip() for line in sys.stdin)

    initial_string_list = [string for string in binary_strings]
    string_length = len(initial_string_list[0])
    print("\n", "-" * 20, "oxygen generator", "-" * 20, end = "\n"*2)
    oxy_gen = recursion_with_branch(count_and_split_strings, initial_string_list, [], 1, string_length -1)

    print("\n", "-" * 20, "CO2 scrubber", "-" * 20, end = "\n"*2)
    co2_scrubber = recursion_with_branch(count_and_split_strings, [], initial_string_list, 0, string_length - 1)

    print(oxy_gen * co2_scrubber)

    
        
