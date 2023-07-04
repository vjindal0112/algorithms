from algorithms.binary_search import binary_search


class TestBinarySearch:
    def test_large(self) -> None:
        data = [1, 3, 5, 2, 5, 7, 4, 99, 76, 54, 33, 43, 6543, 221,
                123, 32, 12, 41, 321, 2451, 123, 12, 43, 53, 46,
                57, 68, 78, 213, 45, 32, 68, 987, 324, 17, 15,
                27, 82, 39, 92, 27, 26, 52, 15]
        data.sort()
        assert binary_search(data, 54) == data.index(54)

    def test_last(self) -> None:
        data = [1, 24, 34, 43, 45, 46, 54]
        data.sort()
        assert binary_search(data, 54) == data.index(54)

    def test_first(self) -> None:
        data = [54, 765, 543, 543, 124, 234, 346, 457, 578, 6798]
        data.sort()
        assert binary_search(data, 54) == data.index(54)

    def test_dups(self) -> None:
        data = [1, 24, 34, 43, 45, 46, 54, 1, 24, 34, 43, 45, 46, 54]
        data.sort()
        assert binary_search(data, 54 - 1) == data.index(54)

    def test_small(self) -> None:
        data = [1, 44, 47, 54, 65, 85, 99]
        data.sort()
        assert binary_search(data, 54) == data.index(54)

    def test_not_exist(self) -> None:
        data = [1, 4, 5, 76, 8, 6, 457, 87]
        data.sort()
        assert binary_search(data, 3) == 1
