#!/usr/bin/env python3

import numpy as np
import heapq

DEBUG = {0}
DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]

def debug_print(string, debug_level):
    if debug_level in DEBUG:
        print(string)

class HeapDijkstras:

    def __init__(self, target, source, distances):
        self.check_next = []
        self.path_lengths_seen = {source : 0}
        self.distances = distances
        self.target_node = target

        debug_print(str(self.path_lengths_seen), 1)
        
        #initialise heap
        self._push_viable_nodes_on_heap((0, source))


        
    def _is_viable_node(self, node):
        def test(test_value, test_index):
            return test_value > -1 and test_value < self.distances.shape[test_index]

        debug_print([test(axis_value, axis_index) for axis_index, axis_value in enumerate(node)], 1)
        
        return all([test(axis_value, axis_index) for axis_index, axis_value in enumerate(node)])
            
    def _push_on_heap_and_update_seen(self, node, node_length):
        self.path_lengths_seen[node] = node_length
        heapq.heappush(self.check_next, (node_length, node))
            
    def _push_viable_nodes_on_heap(self, heap_element):
        heap_value = heap_element[0]
        source_node = heap_element[1]

        debug_print(heap_element, 1)
        
        for direction in DIRECTIONS: 
            possible_node = tuple([elem+direction[index] for index, elem in enumerate(source_node)])

            if self._is_viable_node(possible_node):
                debug_print(possible_node, 1)
                possible_node_length = self.distances[possible_node] + self.path_lengths_seen[source_node]
                if possible_node in self.path_lengths_seen:
                    if self.path_lengths_seen[possible_node] > possible_node_length:
                        self._push_on_heap_and_updatxe_seen(possible_node, possible_node_length)

                else:
                    self._push_on_heap_and_update_seen(possible_node, possible_node_length)

    def find_shortest_path_to_target(self):
        while self.check_next:
            debug_print(self.check_next, 1)
            next_heap_element = heapq.heappop(self.check_next)
            self._push_viable_nodes_on_heap(next_heap_element)

        debug_print(self.path_lengths_seen, 0)
        return self.path_lengths_seen[self.target_node]
        

def load_into_array(data):
    risk_array = np.array(data)
    return risk_array


if __name__ == "__main__":
    with open("./Advent Of Code data/AOC15", "r") as infile:
        data = [line.rstrip() for line in infile]
        
    risk_int_strips = [[int(char) for char in line] for line in data]
    risk_array = load_into_array(risk_int_strips)

    i,j = risk_array.shape
    entrance_node = (i-1, j-1)
    exit_node = (0, 0)
    
    graph = HeapDijkstras(entrance_node, exit_node, risk_array)
    print(graph.find_shortest_path_to_target())
    
