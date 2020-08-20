import random


def build_graph(input):
    vertices = []
    edges = []

    for line in input.split('\n'):
        if not line:
            continue

        row = line.split()
        vertex = row.pop(0)

        vertices.append(vertex)

        for other_vertex in row:
            if other_vertex in vertices:
                continue
            edges.append([vertex, other_vertex])

    return vertices, edges


def min_cut(g):
    vertices, edges = g

    while len(vertices) > 2:
        popped_edge = edges.pop(random.randrange(len(edges)))

        u, v = popped_edge

        vertices.pop(vertices.index(v))

        for edge in edges:
            if edge[0] == v:
                edge[0] = u
            if edge[1] == v:
                edge[1] = u

        edges[:] = [edge for edge in edges if edge[0] != edge[1]]

    return edges


def loop_min_cut(g):
    best = None
    n_best = len(g[1])

    n = len(g[0])

    iterations = n * n

    for i in range(iterations):

        g_copy = (g[0][:], [edge[:] for edge in g[1]])

        result = min_cut(g_copy)
        n_result = len(result)

        if n_result < n_best:
            best = result
            n_best = n_result

    return best


def main():
    with open('kargerMinCut.txt') as f:
        g = build_graph(f.read())

        print(len(loop_min_cut(g)))


main()
