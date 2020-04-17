def earliest_ancestor(ancestors, starting_node):
    hm = {}
    paths = []
    visited = set()

    # build our graph using children as keys
    for ancestor in ancestors:
        x, y = ancestor
        if y not in hm:
            hm[y] = set()
        hm[y].add(x)

    # dft looking for max parent
    def find_ancestor(starting_node, path=None):
        if path is None:
            path = [starting_node]

        if path[-1] in hm and path[-1] not in visited:
            visited.add(path[-1])
            for next_vert in hm[path[-1]]:
                # add our new path to paths list since we don't care about shorter paths
                new_path = path + [next_vert]
                paths.append(new_path)
                find_ancestor(next_vert, new_path)

    find_ancestor(starting_node)

    smallest = None
    if len(paths) > 0:  # if our paths list has items, find the smallest
        max_length = max(map(len, paths))
        max_length_paths = [p for p in paths if len(p) is max_length]

        for path in max_length_paths:
            if smallest is None:
                smallest = path[-1]
            elif path[-1] < smallest:
                smallest = path[-1]

    if smallest:
        return smallest
    else:
        return -1
