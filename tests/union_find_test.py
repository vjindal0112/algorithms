from algorithms.union_find import union_find, Node


class TestUnionFind:
    def test_simple(self) -> None:
        n1 = Node()
        n2 = Node()
        n3 = Node()
        n4 = Node()
        n1.parent = n2
        n3.parent = n4
        assert union_find([n1, n2, n3, n4]) == 2

    def test_tree(self) -> None:
        n1 = Node()
        n2 = Node()
        n3 = Node()
        n4 = Node()
        n5 = Node()
        n1.parent = n2
        n3.parent = n4
        n2.parent = n5
        n4.parent = n5
        assert union_find([n1, n2, n3, n4, n5]) == 1

    def test_disconnected(self) -> None:
        n1 = Node()
        n2 = Node()
        n3 = Node()
        n4 = Node()
        n5 = Node()
        assert union_find([n1, n2, n3, n4, n5]) == 5

    def test_linked_list(self) -> None:
        n1 = Node()
        n2 = Node()
        n3 = Node()
        n4 = Node()
        n5 = Node()
        n1.parent = n2
        n2.parent = n3
        n3.parent = n4
        assert union_find([n1, n2, n3, n4, n5]) == 2

    def test_tree_branch(self) -> None:
        n1 = Node()
        n2 = Node()
        n3 = Node()
        n4 = Node()
        n5 = Node()
        n6 = Node()
        n7 = Node()
        n1.parent = n2
        n3.parent = n4
        n2.parent = n5
        n4.parent = n5
        n5.parent = n6
        n6.parent = n7
        assert union_find([n1, n2, n3, n4, n5, n6, n7]) == 1
