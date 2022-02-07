#!/usr/bin/env python3
from collections import Counter
import itertools


NUMBER_OF_STEPS = 40

#itertools receipe
def pairwise(iterable):
    a,b = itertools.tee(iterable)
    next(b, None)
    return zip(a,b)

def convert_pair_rules_to_two_char(pair_rules):
    return {pair:[pair[0]+insert_value, insert_value+pair[1]] for pair, insert_value in pair_rules.items()}
    
def convert_state_to_two_char_counter(state):
    """conver state into a counter of the adjacent character pairs."""
    state_stream = (char for char in state)
    two_char_stream = ("".join((stream_1, stream_2)) for stream_1, stream_2 in pairwise(state_stream))

    state_counter = Counter(two_char_stream)
    return state_counter
        
def perform_polymerisation_step_using_counters(state_counter, pair_rules):
    """apply the step to the state stored in a two character pair counter"""
    next_state_counter = Counter()
    for pair, count in state_counter.items():
        for next_pair in pair_rules[pair]:
            next_state_counter[next_pair] += count
    return next_state_counter

def count_actual_char_occurances(state_counter, inital_state):
    """deduplicate all the characters in the state counter."""
    actual_char_counts = Counter()
    for char_pair, pair_count in state_counter.items():
        for char in char_pair:
            actual_char_counts[char] += pair_count

    # first and last char of string only have one occurance
    actual_char_counts[initial_state[0]] += 1
    actual_char_counts[initial_state[-1]] += 1

    for k, v in actual_char_counts.items():
        actual_char_counts[k] = v/2

    return actual_char_counts


if __name__ == "__main__":

    with open("./Advent Of Code data/AOC14", "r") as infile:
        data = [line.rstrip() for line in infile]

    initial_state = data[0]
    state_counter = convert_state_to_two_char_counter(initial_state)
    
    pair_rule_data = [[pair_instruction for pair_instruction in line.split(" -> ")] for line in data[2:]]
    pair_rules = {k:v for k,v in pair_rule_data}
    two_char_pair_rules = convert_pair_rules_to_two_char(pair_rules)


    for i in range(NUMBER_OF_STEPS):
        state_counter = perform_polymerisation_step_using_counters(state_counter, two_char_pair_rules)
        print("step: ", i+1, "  ", state_counter)

    char_counts = count_actual_char_occurances(state_counter, initial_state)
    print((char_counts.most_common())[0][1] - (char_counts.most_common())[-1][1])
    
