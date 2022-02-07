#!/usr/bin/env python3
import collections

DEBUG = 1

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

matching_bracket_map = {
    
    '(' : ')',
    '{' : '}',
    '[' : ']',
    '<' : '>'
    }

score_per_bracket_2 = {
    
    ')' : 1,
    '}' : 3,
    ']' : 2,
    '>' : 4
    }
    

def debug_print(print_string, is_debug_on=DEBUG):
    if is_debug_on:
        print(print_string)

def test_illegal_bracket_in_string(bracket_string):
    bracket_stack = []
    bracket_to_match = None
    for char in bracket_string:
        if push_pop_map[char]:
            bracket_stack.append(char)
        else:
            bracket_to_match = bracket_stack.pop()
            if score_per_bracket_map[bracket_to_match] != score_per_bracket_map[char]:
                #debug_print("expected {}, but found {} instead".format(bracket_to_match, char))
                return 0
    return 1

def return_incomplete_bracket_string(bracket_string):
    if test_illegal_bracket_in_string(bracket_string):
        return bracket_string

def complete_incomplete_bracket_string(bracket_string):
    bracket_stack = []
    for char in bracket_string:
        if push_pop_map[char]:
            bracket_stack.append(char)
        else:
            bracket_stack.pop()

    bracket_stack.reverse()
    debug_print("{} + {}".format(bracket_string, "".join([matching_bracket_map[char] for char in bracket_stack])))
    return "".join([matching_bracket_map[char] for char in bracket_stack])
    

if __name__ == "__main__":

    with open("./Advent Of Code data/AOC10", "r")  as infile:
        data = [line.rstrip() for line in infile.readlines()]

    incomplete_bracket_strings = [return_incomplete_bracket_string(line) for line in data]
    incomplete_bracket_strings = [bracket_string for bracket_string in incomplete_bracket_strings if bracket_string is not None]

    debug_print(incomplete_bracket_strings)

    string_completion_scores = []
    for bracket_string in incomplete_bracket_strings:
        string_completion = complete_incomplete_bracket_string(bracket_string)

        score = 0
        for char in string_completion:
            score *= 5
            score += score_per_bracket_2[char]
        
        string_completion_scores.append(score)

    string_completion_scores.sort()
    print(string_completion_scores)
    print(string_completion_scores[round(len(string_completion_scores)/2)])
