#!/usr/bin/python3
import sys
import collections
import itertools

string_count_to_numeral_set = {
    2 : {1},
    3 : {7},
    4 : {4},
    5 : {2, 3, 5},
    6 : {0, 6, 9},
    7 : {8}
}
"""
    display positions
         0000
         1  2
         1  2
         3333
         4  5
         4  5
         6666 
 """

numeral_to_display_position_set = {
    0 : {0, 1, 2, 4, 5 ,6},
    1 : {2, 5},
    2 : {0, 2, 3, 4, 6},
    3 : {0, 2, 3, 5, 6},
    4 : {1, 2, 3, 5},
    5 : {0, 1, 3, 5, 6},
    6 : {0, 1, 3, 4, 5, 6},
    7 : {0, 2, 5},
    8 : {0, 1, 2, 3, 4, 5, 6},
    9 : {0, 1, 2, 3, 5, 6}
}


def count_number_of_string_lengths(strings_list):
    string_counter = collections.Counter()

    string_counter.update([len(string) for strings in strings_list for string in strings])

    return string_counter

def break_signals_to_fragments(signals):
    return (signal.split(" ") for signal in signals)

def recover_display_positions_from_numerals(numeral_set):
    display_position_set = set()
    for numeral in numeral_set:
        display_position_set = display_position_set.union(numeral_to_display_position_set[numeral])
    return display_position_set

def determine_signal_display_positions(strings):
    signals = dict()
    
    for string in strings:
        numeral_set = string_count_to_numeral_set[len(string)]
            
        for character in string:
            if character in signals:
                character_set = signals[character]
                signals[character] = character_set.intersection(recover_display_positions_from_numerals(numeral_set))
            else:
                signals[character] = recover_display_positions_from_numerals(numeral_set)
    return signals

if __name__ == "__main__":

    signal_outputs_io = (line.rstrip() for line in sys.stdin)
    signal_patterns = (signal_output.split(" | ") for signal_output in signal_outputs_io)
    signals_train = (signal_pattern[0] for signal_pattern in signal_patterns)
    signals_test = (signal_pattern[1] for signal_pattern in signal_patterns)

    signal_fragments_train = break_signals_to_fragments(signals_train)

    for strings in signal_fragments_train:
        print(strings, determine_signal_display_positions(strings))
