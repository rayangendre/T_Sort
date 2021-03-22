from sys import argv
from stack_array import *


def tsort(vertices):
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * identically to the Unix utility "tsort".  That is, one vertex per
    * line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"'''

    if vertices is None or vertices == []:
        raise ValueError('input contains no edges')

    if len(vertices) % 2 != 0:
        raise ValueError('input contains an odd number of tokens')

    dict_vert = {}

    for i in range(0, len(vertices), 2):
        first_vertex = vertices[i]
        second_vertex = vertices[i + 1]

        if not dict_vert:
            dict_vert[first_vertex] = [0, second_vertex]
            if not dict_vert.get(second_vertex):
                dict_vert[second_vertex] = [1]
        else:
            if not dict_vert.get(first_vertex):
                dict_vert[first_vertex] = [0, second_vertex]
            else:
                dict_vert[first_vertex].append(second_vertex)

            if not dict_vert.get(second_vertex):
                dict_vert[second_vertex] = [1]
            else:
                dict_vert[second_vertex][0] += 1

    stack = Stack(100)
    ordered_list = ''

    dict_keys = dict_vert.keys()
    for y in dict_keys:
        if dict_vert.get(y)[0] == 0:
            stack.push(y)

    while not stack.is_empty():
        popped_vert = stack.pop()
        adjacency_list = dict_vert.get(popped_vert)[1:]

        for j in adjacency_list:
            temp_val = dict_vert.get(j)
            temp_val = temp_val[0] - 1
            dict_vert[j][0] = temp_val

            if temp_val == 0:
                    stack.push(j)

        ordered_list = ordered_list + '\n' + popped_vert

    compare_list = ordered_list.split()
    if len(compare_list) == len(dict_keys):
        return ordered_list
    else:
        raise ValueError('input contains a cycle')


def main():
    '''Entry point for the tsort utility allowing the user to specify
       a file containing the edge of the DAG'''
    if len(argv) != 2:
        print("Usage: python3 tsort.py <filename>")
        exit()
    try:
        f = open(argv[1], 'r')
    except FileNotFoundError as e:
        print(argv[1], 'could not be found or opened')
        exit()

    vertices = []
    for line in f:
        vertices += line.split()

    try:
        result = tsort(vertices)
        print(result)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
