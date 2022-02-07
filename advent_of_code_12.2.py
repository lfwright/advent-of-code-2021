#!/usr/bin/env python3
import collections

DEBUG = {}

def debug_print(print_string, group):
    if group in DEBUG:
        print(print_string)

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

def find_graph_paths(graph, max_vists):

    max_node_vists = collections.Counter({k:max_vists for k,v in graph.items() if k not in {'start', 'end'} and k.islower()})
    max_node_vists.update({k:9999 for k,v in graph.items() if k not in {'start', 'end'} and not k.islower()})
    max_node_vists['end'] = 1
    max_node_vists['start'] = 1
    
    paths_to_evaluate = collections.deque()
    paths_to_evaluate.append({0:'start', 'start':1}) # 0 is the next node

    paths_to_end_count = 0

    while paths_to_evaluate:
        
        debug_print(paths_to_evaluate, 1)
        current_path = paths_to_evaluate.popleft()



        # check if the vist small cave twice once condition is met
        for head in range(2):
            debug_print(graph.get(current_path.get(head, 0), []), 1)
            for next_node in graph.get(current_path.get(head, 0), []):
                if next_node == 'end':
                    paths_to_end_count += 1
                    print(paths_to_end_count, current_path)
                    
                elif current_path.get(next_node, 0) < max_node_vists[next_node] - head:
                    next_path = {} # force new object
                    next_path.update(current_path)
                    del next_path[head]
                    
                    next_path[next_node] = 1+next_path.get(next_node, 0)

                    next_head = 1 if next_path[next_node] == max_node_vists[next_node] else max(0, head)
                    next_path[next_head] = next_node
                    
                    paths_to_evaluate.append(next_path)


    return paths_to_end_count
                
    
                
if __name__ == "__main__":

    with open("./Advent Of Code data/AOC12", "r") as infile:
        data = [line.rstrip().split("-") for line in infile]

    graph = build_graph(data)
    print(graph, end="\n")

    
    path_count = find_graph_paths(graph, 2)
    print(path_count)
    
