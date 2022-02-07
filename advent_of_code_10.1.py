#!/usr/bin/env python3
import collections

DEBUG = 0

push_pop_map = {
    '(' : 1, #push
    '{' : 1,
    '[' : 1,
    '<' : 1,

    ')' : 0, #pop
    '}' : 0,
    ']' : 0,
    '>' : 0
    }

score_per_bracket_map = {
    0 : 0, #handle 0 KeyErrors
    
    '(' : 3,
    '{' : 1197,
    '[' : 57,
    '<' : 25137,

    ')' : 3,
    '}' : 1197,
    ']' : 57,
    '>' : 25137
    }

def debug_print(print_string, is_debug_on=DEBUG):
    if is_debug_on:
        print(print_string)

def extract_illegal_bracket_in_string(bracket_string):
    bracket_stack = []
    bracket_to_match = None
    for char in bracket_string:
        if push_pop_map[char]:
            bracket_stack.append(char)
        else:
            bracket_to_match = bracket_stack.pop()
            if score_per_bracket_map[bracket_to_match] != score_per_bracket_map[char]:
                debug_print("expected {}, but found {} instead".format(bracket_to_match, char))
                return char
    return 0 

if __name__ == "__main__":

    with open("./Advent Of Code data/AOC10", "r")  as infile:
        data = [line.rstrip() for line in infile.readlines()]

    illegal_bracket_counter = collections.Counter()
    for line in data:
        first_illegal_bracket = extract_illegal_bracket_in_string(line)
        illegal_bracket_counter[first_illegal_bracket] += 1

    bracket_score = 0
    for bracket, bracket_count in illegal_bracket_counter.items():
        print("there were {} illegal {}".format(bracket_count, bracket))
        bracket_score += bracket_count*score_per_bracket_map[bracket]

    print("final score: ", bracket_score)
        
