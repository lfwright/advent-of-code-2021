#!/usr/bin/python3

## should probably do this in binary somehow
## oh well
import sys

def extract_bit(binary_to_check, n):
    mask = 1 << n # create binary string with 1 in nth position
    extract_bit = int(binary_to_check,2) & mask # extract the nth position from the input string
    return extract_bit >> n # return 0 or 1
    

if __name__ == '__main__':

    binary_strings = (line for line in sys.stdin)

    number_of_strings = 0
    bit_position_counts = dict()
    
    for string in binary_strings:
        number_of_strings += 1
        
        length_of_string = len(string)
        for element in range(length_of_string):
            extracted_bit = extract_bit(string, element)
            if extracted_bit > 1:
                print('extracted bit was greater than 1')
            bit_position_counts[element] = bit_position_counts.get(element, 0) + extracted_bit

    most_common_test = number_of_strings / 2
    gamma_rate = 0

    for k, v in bit_position_counts.items():
        if v > most_common_test: #test the count of the position
            gamma_rate += (1 << k) #create a 1 in the tested position

    gamma_string_size = len(bin(gamma_rate)) - 2
    epsilon_rate = (int('1' * gamma_string_size,2) ^ gamma_rate) # use gamma XOR 1 string to find where the 0's are

    print("gamma_rate", gamma_rate, bin(gamma_rate))
    print("epsilon_rate", epsilon_rate, bin(epsilon_rate))

    #print answer
    print(gamma_rate * epsilon_rate)
        
