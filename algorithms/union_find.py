class Node:
    def __init__(self) -> None:
        self.parent = self


def union(node1: Node, node2: Node) -> Node:
    root1 = find(node1)
    root2 = find(node2)
    root1.parent = root2
    return root2


def find(node: Node) -> Node:
    temp_node = node
    while temp_node.parent != temp_node:
        temp_node = temp_node.parent
    return temp_node


def union_find(all_nodes: list[Node]) -> int:
    parents = [x for x in range(len(all_nodes))]
    node_to_index = {node: index for index, node in enumerate(all_nodes)}
    index_to_node = {index: node for index, node in enumerate(all_nodes)}
    count = 0
    for node in all_nodes:
        parents[count] = node_to_index[find(node)]
        count += 1

    distinct_parents = set()
    for parent in parents:
        distinct_parents.add(find(index_to_node[parent]))

    return len(distinct_parents)
