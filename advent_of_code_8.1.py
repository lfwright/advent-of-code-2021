#!/usr/bin/python3
import sys
import collections

string_count_to_numeral = {
    2 : {1},
    3 : {7},
    4 : {4},
    5 : {2, 3, 5},
    6 : {0, 6, 9},
    7 : {8}
}

def count_number_of_string_lengths(strings_list):
    string_counter = collections.Counter()

    string_counter.update([len(string) for strings in strings_list for string in strings])

    return string_counter

if __name__ == "__main__":

    signal_outputs_io = (line.rstrip() for line in sys.stdin)
    signal_patterns = (signal_output.split(" | ") for signal_output in signal_outputs_io)
    signals = (signal_pattern[1] for signal_pattern in signal_patterns)
    signal_fragments = (signal.split(" ") for signal in signals)
    
    signal_counter = count_number_of_string_lengths(signal_fragments)

    for k,v in string_count_to_numeral.items():
        print("the set of numerals {} occurs {} times.".format(v, signal_counter[k]))
