#!/usr/bin/env python3
from collections import Counter


def perform_polymerisation_step(state, pair_rules):
    post_step_state_array = list(state)
    insert_counter = 0

    insert_characters = [[index, pair_rules[state[index: index+2]]] for index, char in enumerate(state[:-1])]

    for insert_index, char in insert_characters:
        post_step_state_array.insert(insert_index+insert_counter+1, char)
        insert_counter += 1

    return "".join(post_step_state_array)

if __name__ == "__main__":

    with open("./Advent Of Code data/AOC14 example", "r") as infile:
        data = [line.rstrip() for line in infile]

    state = data[0]
    pair_rule_data = [[pair_instruction for pair_instruction in line.split(" -> ")] for line in data[2:]]

    pair_rules = {k:v for k,v in pair_rule_data}

    for i in range(10):
        state = perform_polymerisation_step(state, pair_rules)
        print(state)

    print(Counter(state))

    
