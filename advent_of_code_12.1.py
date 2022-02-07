#!/usr/bin/env python3
import collections


def build_graph(pair_list):
    
    graph = dict()

    for node_pair in pair_list:
        for node_pair_index in range(2):
            if node_pair[node_pair_index] in graph:
                neighbours = graph[node_pair[node_pair_index]]
                neighbours.add(node_pair[(node_pair_index+1) % 2])
                graph[node_pair[node_pair_index]] = neighbours
            else:
                graph[node_pair[node_pair_index]] = {node_pair[(node_pair_index+1) % 2]}
 
    return graph

def find_graph_paths(graph, node_to_evaluate, current_path):

    if node_to_evaluate == 'end':
        for node in (current_path[1:-1]):
            print(node, end="->")
        print('end')
        return current_path

    path_counter = collections.Counter()
    
    #seen_nodes is passed as a tuple so that it is imutatable
    seen_nodes = set([node for node in current_path if node.islower()])
    seen_nodes.add(node_to_evaluate)
    
    for next_node in graph[node_to_evaluate]:
        if next_node not in seen_nodes:
            path_counter.update(find_graph_paths(graph, next_node, (*current_path, next_node)))

    return path_counter

    
                
if __name__ == "__main__":

    with open("./Advent Of Code data/AOC12", "r") as infile:
        data = [line.rstrip().split("-") for line in infile]

    graph = build_graph(data)
    print(graph)

    path_counter = find_graph_paths(graph, ('start'), ('', 'start'))
    print(path_counter)
    # we will answer this with a recursive function
    # 
