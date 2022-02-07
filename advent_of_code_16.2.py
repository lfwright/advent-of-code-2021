#!/usr/bin/env python3

from functools import reduce
from operator import lt, gt, eq, add

DEBUG = {2,3}
PACKET_TYPE_MAP = {
    0: 'sum',
    1: 'product',
    2: 'minimum',
    3: 'maximum',
    4: 'literal',
    5: 'greater than',
    6: 'less than',
    7: 'equal to',
    }

FUNCTION_MAP = {
    'sum': add,
    'product': lambda x, y=1: x*y,
    'minimum': min,
    'maximum': max,
    'greater than': gt,
    'less than': lt,
    'equal to': eq
    }
    

def debug_print(print_string, debug_level):
    if debug_level in DEBUG:
        print(print_string)

def convert_hexadecimal_to_binary(hex_string):
    '''return binary representation of inputted hex string.'''
    binary_length = len(hex_string)*4
    value = int(hex_string, 16)
    spec = '0{}b'.format(binary_length)
    debug_print((binary_length, hex_string, spec), 0)
    return format(value, spec)

def request_bits_from_stream(bit_stream, request_length):
    '''Return the requested number of bits from the stream'''
    binary_string = ''
    for i in range(request_length):
        next_bit = next(bit_stream)
        binary_string += next_bit
    return binary_string

def get_packet_version(binary_string):
    '''Return the version number.'''
    debug_print("packet version-"+binary_string, 0)
    return int(binary_string, 2)
    
def get_packet_type(binary_string):
    '''Return the version number.'''
    debug_print("packet type-"+binary_string, 0)    
    return int(binary_string, 2)


def read_literal_packet(version_number, bit_stream):
    read_more = 1
    request_count = 6 # version + type
    literal_string = ''
    
    while read_more:
        literal_group = request_bits_from_stream(bit_stream, 5)
        request_count += 1
        
        literal_string += literal_group[1:5]

        read_more = int(literal_group[0], 2)
        
    # request the padding to clean bit stream
    # find the number of bits needed to pad to a multipe of 4
    #padding_bits = (4 - (request_count*5 % 4)) % 4 
    #debug_string = 'tossed - ' + request_bits_from_stream(bit_stream, padding_bits)

    literal_value = int(literal_string, 2)
    print('LITERAL -- VERSION {version} -- {value}'.format(version=version_number, value=literal_value))
    #debug_print(debug_string, 0)
    return literal_value

def read_operator_packet(version_number, packet_type, bit_stream):
    request_count = 6 # version + type
    length_type_id = int(request_bits_from_stream(bit_stream, 1), 2)

    request_count += 1
    
    length_bits_request =  11 if length_type_id else 15
    length_bits = request_bits_from_stream(bit_stream, length_bits_request)

    request_count += length_bits_request
    
    payload_length = int(length_bits, 2)
    debug_print(('payload ' + str(payload_length), 'length_type ' + str(length_type_id)), 1)
    print('OPERATOR {packet_t} -- VERSION {version} -- LENGTH TYPE {length_t} -- ('
          .format(packet_t=packet_type, version=version_number, length_t=length_type_id))
    if length_type_id:
        debug_print('packet method', 1)
        operator_arguments = read_packets(bit_stream, payload_length)

    else:
        debug_print('bit method', 1)
        payload_bit_stream = (bit for bit in request_bits_from_stream(bit_stream, payload_length))
        operator_arguments = read_packets(payload_bit_stream, -1)

    print(')')

    debug_print((packet_type, operator_arguments), 3)
    if packet_type in {'sum', 'product', 'minimum', 'maximum'}:
        operation_value = reduce(FUNCTION_MAP[packet_type], operator_arguments)
    else:
        operation_value = FUNCTION_MAP[packet_type](*operator_arguments)

    debug_print(operation_value, 3)
    return operation_value
    

    
def read_packet(bit_stream):
    packet_version = get_packet_version(request_bits_from_stream(bit_stream, 3))
    packet_type = get_packet_type(request_bits_from_stream(bit_stream, 3))
    
    if PACKET_TYPE_MAP[packet_type] == 'literal':
        packet_value = read_literal_packet(packet_version, bit_stream)
    else:
        packet_value = read_operator_packet(packet_version,PACKET_TYPE_MAP[packet_type], bit_stream)

    return packet_value


def read_packets(bit_stream, finite_count):
    packet_count = 0
    packet_values = []
    try:
        if finite_count < 0:
            debug_print('infinite stream', 2)
            while bit_stream:
                packet_value = read_packet(bit_stream)
                packet_values.append(packet_value)

                packet_count += 1
            debug_print(packet_count, 0)
        else:
            debug_print('finite stream', 2)
            while bit_stream and finite_count > 0:
                packet_value = read_packet(bit_stream)
                packet_values.append(packet_value)                

                finite_count -= 1
                packet_count += 1
            debug_print(packet_count, 0)
    except StopIteration:
        print('finished reading stream.')
    return packet_values
def main():
    with open('./Advent Of Code data/AOC16', 'r') as in_file:
        hexadecimal_transmission = in_file.read().strip()

    binary_transmission = convert_hexadecimal_to_binary(hexadecimal_transmission)
    debug_print(binary_transmission, 0)
    debug_print(len(binary_transmission), 0)
    bit_stream = (bit for bit in binary_transmission)

    read_packets(bit_stream, -1)


if __name__ == '__main__':
    main()
    
